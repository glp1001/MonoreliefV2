import argparse
import cv2
import glob
import matplotlib
import os
import torch
from depth_anything_v2.dpt import DepthAnythingV2
import numpy as np
from tqdm.auto import tqdm
import pyvista as pv
from peft import  PeftModel, PeftConfig


# Define helper functions for moving masks in different directions
def move_left(mask): return np.pad(mask,((0,0),(0,1)),'constant',constant_values=0)[:,1:]  # Shift the input mask array to the left by 1, filling the right edge with zeros.
def move_right(mask): return np.pad(mask,((0,0),(1,0)),'constant',constant_values=0)[:,:-1]  # Shift the input mask array to the right by 1, filling the left edge with zeros.
def move_top(mask): return np.pad(mask,((0,1),(0,0)),'constant',constant_values=0)[1:,:]  # Shift the input mask array up by 1, filling the bottom edge with zeros.
def move_bottom(mask): return np.pad(mask,((1,0),(0,0)),'constant',constant_values=0)[:-1,:]  # Shift the input mask array down by 1, filling the top edge with zeros.
def move_top_left(mask): return np.pad(mask,((0,1),(0,1)),'constant',constant_values=0)[1:,1:]  # Shift the input mask array up and to the left by 1, filling the bottom and right edges with zeros.
def move_top_right(mask): return np.pad(mask,((0,1),(1,0)),'constant',constant_values=0)[1:,:-1]  # Shift the input mask array up and to the right by 1, filling the bottom and left edges with zeros.
def move_bottom_left(mask): return np.pad(mask,((1,0),(0,1)),'constant',constant_values=0)[:-1,1:]  # Shift the input mask array down and to the left by 1, filling the top and right edges with zeros.
def move_bottom_right(mask): return np.pad(mask,((1,0),(1,0)),'constant',constant_values=0)[:-1,:-1]

def construct_facets_from(mask):
    # Initialize an array 'idx' of the same shape as 'mask' with integers
    # representing the indices of valid pixels in the mask.
    idx = np.zeros_like(mask, dtype=int)
    idx[mask] = np.arange(np.sum(mask))

    # Generate masks for neighboring pixels to define facets
    facet_move_top_mask = move_top(mask)
    facet_move_left_mask = move_left(mask)
    facet_move_top_left_mask = move_top_left(mask)

    # Identify the top-left pixel of each facet by performing a logical AND operation
    # on the masks of neighboring pixels and the input mask.
    facet_top_left_mask = np.logical_and.reduce((facet_move_top_mask, facet_move_left_mask, facet_move_top_left_mask, mask))

    # Create masks for the other three vertices of each facet by shifting the top-left mask.
    facet_top_right_mask = move_right(facet_top_left_mask)
    facet_bottom_left_mask = move_bottom(facet_top_left_mask)
    facet_bottom_right_mask = move_bottom_right(facet_top_left_mask)

    return np.stack((4 * np.ones(np.sum(facet_top_left_mask)),
               idx[facet_top_left_mask],
               idx[facet_bottom_left_mask],
               idx[facet_bottom_right_mask],
               idx[facet_top_right_mask]), axis=-1).astype(int)


def map_depth_map_to_point_clouds(depth_map, mask, K=None, step_size=1):
    # y
    # |  z
    # | /
    # |/
    # o ---x
    H, W = mask.shape
    yy, xx = np.meshgrid(range(W), range(H))
    xx = np.flip(xx, axis=0)

    if K is None:
        vertices = np.zeros((H, W, 3))
        vertices[..., 0] = yy * step_size
        vertices[..., 1] = xx * step_size
        vertices[..., 2] = -depth_map
        vertices = vertices[mask]
    else:
        u = np.zeros((H, W, 3))
        u[..., 0] = yy
        u[..., 1] = xx
        u[..., 2] = 1
        u = u[mask].T  # 3 x m
        vertices = -(np.linalg.inv(K) @ u).T * depth_map[mask, np.newaxis]  # m x 3

    return vertices


def depth2normal(depth_map):
    kernel_x = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])
    kernel_y = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])

    gx = cv2.filter2D(depth_map, -1, kernel_x)
    gy = cv2.filter2D(depth_map, -1, kernel_y)

    gx = gx / 8
    gy = gy / 8

    mo = np.sqrt(gx * gx + gy * gy + 1)

    depth_normal = np.stack([gx / mo, gy / mo, 1 / mo], axis=2)
    return depth_normal

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Depth Anything V2')
    
    parser.add_argument('--img-path', default=r"D:\gaolipeng\Depth-Anything-V2-main\assets\real",type=str)
    parser.add_argument('--input-size', type=int, default=1022)
    parser.add_argument('--outdir', type=str, default="./out")
    parser.add_argument('--encoder', type=str, default='vitb', choices=['vits', 'vitb', 'vitl', 'vitg'])
    parser.add_argument('--ckptdir', type=str, default="./checkpoints/Moreliefv2.pth")
    parser.add_argument('--loradir', type=str, default="./checkpoints/lora")
    parser.add_argument('--pred-only', dest='pred_only', action='store_true', help='only display the prediction')
    parser.add_argument('--grayscale', dest='grayscale', action='store_true', help='do not apply colorful palette')

    args = parser.parse_args()
    
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    model_configs = {
        'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
        'vitb': {'encoder': 'vitb', 'features': 128, 'out_channels': [96, 192, 384, 768]},
        'vitl': {'encoder': 'vitl', 'features': 256, 'out_channels': [256, 512, 1024, 1024]},
        'vitg': {'encoder': 'vitg', 'features': 384, 'out_channels': [1536, 1536, 1536, 1536]}
    }
    
    depth_anything = DepthAnythingV2(**model_configs[args.encoder])
    model_id = args.loradir
    config = PeftConfig.from_pretrained(model_id)
    depth_anything.load_state_dict(torch.load(args.ckptdir,
                   map_location='cpu'))
    inference_model = PeftModel.from_pretrained(depth_anything, model_id)
    inference_model.to(DEVICE).eval()
    if os.path.isfile(args.img_path):
        if args.img_path.endswith('txt'):
            with open(args.img_path, 'r') as f:
                filenames = f.read().splitlines()
        else:
            filenames = [args.img_path]
    else:
        filenames = glob.glob(os.path.join(args.img_path, '**/*'), recursive=True)
    
    os.makedirs(args.outdir, exist_ok=True)
    
    cmap = matplotlib.colormaps.get_cmap('Spectral_r')
    
    for k, filename in tqdm(enumerate(filenames)):
        print(f'Progress {k+1}/{len(filenames)}: {filename}')

        name = os.path.join(args.outdir, os.path.splitext(os.path.basename(filename))[0] + '.png')
        # 如果发现文件夹包含了name的浮雕深度图，则跳过
        if os.path.exists(name):
            continue


        raw_image = cv2.imread(filename)
        depth = depth_anything.infer_image(raw_image, args.input_size)
        print(f'Prediction is done！')

        depth = depth - np.min(depth)

        zero_mask = np.ones(depth.shape[:2], bool)
        vertices = map_depth_map_to_point_clouds(-depth, zero_mask, K=None, step_size=1)
        facets = construct_facets_from(zero_mask)
        surface = pv.PolyData(vertices, facets)
        pv.save_meshio(os.path.join(args.outdir, os.path.splitext(os.path.basename(filename))[0] +'.obj'), surface)

        depth_normal = depth2normal(depth)
        cv2.imwrite(os.path.join(args.outdir, os.path.splitext(os.path.basename(filename))[0] + '_normal.png'),
                    cv2.cvtColor((255 * (depth_normal * 0.5 + 0.5)).astype(np.uint8), cv2.COLOR_RGB2BGR))
        print(f'Saving is done！')