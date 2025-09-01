<div align="center">
<h1>MonoRelief V2: Leveraging Real Data for High-Fidelity Monocular Relief Recovery
</h1>

Yu-Wei Zhang<sup>1*&dagger;</sup> · Tongju Han<sup>1</sup> ·Lipeng Gao<sup>1</sup>
<br>
Mingqiang Wei<sup>2</sup> · Hui Liu<sup>3</sup> · Changbao Li<sup>1</sup> · Caiming Zhang<sup>4</sup>

<sup>1</sup>QLU&emsp;&emsp;&emsp;<sup>2</sup>NUAA&emsp;&emsp;&emsp;<sup>3</sup>SDUFE&emsp;&emsp;&emsp;<sup>4</sup>SDU
<br>
&dagger;project lead&emsp;*corresponding author

<a href="https://arxiv.org/abs/2508.19555v1"><img src='https://img.shields.io/badge/arXiv-Monorelief V2-red' alt='Paper PDF'></a>
<a href='Todo'><img src='https://img.shields.io/badge/pretrianModel(Todo)-Monorelief V2-green' alt='pretrianModel'></a>


<p align="left">This paper presents MonoRelief V2, an end-to-end model designed for directly recovering 2.5D reliefs from single images under complex material and illumination variations. In contrast to its predecessor, MonoRelief V1, which was solely trained on synthetic data, MonoRelief V2 incorporates real data to achieve improved robustness, accuracy and efffciency. To overcome the challenge of acquiring large-scale real-world dataset, we generate approximately 15,000 pseudoreal images using a text-to-image generative model, and derive corresponding depth pseudo-labels through fusion of depth and normal predictions. Furthermore, we construct a small-scale real-world dataset (800 samples) via multi-view reconstruction and detail reffnement. MonoRelief V2 is then progressively trained on the pseudo-real and real-world datasets. Comprehensive experiments demonstrate its state-of-the-art performance both in depth and normal predictions, highlighting its strong potential for a range of downstream applications. </p>

## 
<center class="half">
<img src="assets/g1.jpg" width="130"/>
<img src="assets/g1_n.jpg" width="130"/>
<img src="assets/g1.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g2.png" width="130"/>
<img src="assets/g2_n.jpg" width="130"/>
<img src="assets/g2.gif?raw=true" alt="Sublime's custom image" width="130"/>
</center><br>

<center class="half">
<img src="assets/g3.jpg" width="130"/>
<img src="assets/g3_n.jpg" width="130"/>
<img src="assets/g3.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g4.png" width="130"/>
<img src="assets/g4_n.jpg" width="130"/>
<img src="assets/g4.gif?raw=true" alt="Sublime's custom image" width="130"/>
</center><br>

<center class="half">
<img src="assets/g5.jpg" width="130"/>
<img src="assets/g5_n.jpg" width="130"/>
<img src="assets/g5.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g6.jpg" width="130"/>
<img src="assets/g6_n.jpg" width="130"/>
<img src="assets/g6.gif?raw=true" alt="Sublime's custom image" width="130"/>
</center><br>

<center class="half">
<img src="assets/g7.png" width="130"/>
<img src="assets/g7_n.jpg" width="130"/>
<img src="assets/g7.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g8.jpg" width="130"/>
<img src="assets/g8_n.jpg" width="130"/>
<img src="assets/g8.gif?raw=true" alt="Sublime's custom image" width="130"/>
</center><br>

<center class="half">
<img src="assets/g9.jpg" width="130"/>
<img src="assets/g9_n.jpg" width="130"/>
<img src="assets/g9.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g10.jpg" width="130"/>
<img src="assets/g10_n.jpg" width="130"/>
<img src="assets/g10.gif?raw=true" alt="Sublime's custom image" width="130"/>
</center><br>

<center class="half">
<img src="assets/g11.jpg" width="130"/>
<img src="assets/g11_n.jpg" width="130"/>
<img src="assets/g11.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g12.jpg" width="130"/>
<img src="assets/g12_n.jpg" width="130"/>
<img src="assets/g12.gif?raw=true" alt="Sublime's custom image" width="130"/>  
</center><br>

<center class="half">
<img src="assets/g13.jpg" width="130"/>
<img src="assets/g13_n.jpg" width="130"/>
<img src="assets/g13.gif?raw=true" alt="Sublime's custom image" width="130"/>
<img src="assets/g14.jpg" width="130"/>
<img src="assets/g14_n.jpg" width="130"/>
<img src="assets/g14.gif?raw=true" alt="Sublime's custom image" width="130"/>  
</center><br>


## News
- **2025-08-28:** updata readme.
