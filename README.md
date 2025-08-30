<div align="center">
<h1>MonoRelief V2: Leveraging Real Data for High-Fidelity Monocular Relief Recovery
</h1>

Yu-Wei Zhang<sup>1*&dagger;</sup> · Tongju Han<sup>1</sup> ·Lipeng Gao<sup>1</sup>
<br>
Mingqiang Wei<sup>2</sup> · Hui Liu<sup>3</sup> · Changbao Li<sup>1</sup> · Caiming Zhang<sup>4</sup>

<sup>1</sup>QLU&emsp;&emsp;&emsp;<sup>2</sup>NUAA&emsp;&emsp;&emsp;<sup>3</sup>SDUFE&emsp;&emsp;&emsp;<sup>4</sup>SDU
<br>
&dagger;project lead&emsp;*corresponding author

This paper presents MonoRelief V2, an end-to-end model designed for directly recovering 2.5D reliefs from single images under complex material and illumination variations. In contrast to its predecessor, MonoRelief V1, which was solely trained on synthetic data, MonoRelief V2 incorporates real data to achieve improved robustness, accuracy and efffciency. To overcome the challenge of acquiring large-scale real-world dataset, we generate approximately 15,000 pseudoreal images using a text-to-image generative model, and derive corresponding depth pseudo-labels through fusion of depth and normal predictions. Furthermore, we construct a small-scale real-world dataset (800 samples) via multi-view reconstruction and detail reffnement. MonoRelief V2 is then progressively trained on the pseudo-real and real-world datasets. Comprehensive experiments demonstrate its state-of-the-art performance both in depth and normal predictions, highlighting its strong potential for a range of downstream applications. 

<center class="half">
<img src="assets/g1.jpg" width="200"/>
<img src="assets/g1_d.png" width="200"/>
<img src="assets/g1_n.jpg" width="200"/>
  <img src="assets/g1.gif" width="200"/>
</center>

## News
- **2025-08-28:** updata readme.
