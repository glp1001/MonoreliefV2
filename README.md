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
<img src="assets/g1.jpg" width="90"/>
<img src="assets/g1_d.png" width="90"/>
<img src="assets/g1_n.jpg" width="90"/>
<img src="assets/g1.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g2.png" width="90"/>
<img src="assets/g2_d.png" width="90"/>
<img src="assets/g2_n.jpg" width="90"/>
<img src="assets/g2.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>

<center class="half">
<img src="assets/g3.jpg" width="90"/>
<img src="assets/g3_d.png" width="90"/>
<img src="assets/g3_n.jpg" width="90"/>
<img src="assets/g3.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g4.png" width="90"/>
<img src="assets/g4_d.png" width="90"/>
<img src="assets/g4_n.jpg" width="90"/>
<img src="assets/g4.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>

<center class="half">
<img src="assets/g5.jpg" width="90"/>
<img src="assets/g5_d.png" width="90"/>
<img src="assets/g5_n.jpg" width="90"/>
<img src="assets/g5.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g6.jpg" width="90"/>
<img src="assets/g6_d.png" width="90"/>
<img src="assets/g6_n.jpg" width="90"/>
<img src="assets/g6.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>

<center class="half">
<img src="assets/g7.png" width="90"/>
<img src="assets/g7_d.png" width="90"/>
<img src="assets/g7_n.jpg" width="90"/>
<img src="assets/g7.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g8.jpg" width="90"/>
<img src="assets/g8_d.png" width="90"/>
<img src="assets/g8_n.jpg" width="90"/>
<img src="assets/g8.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>

<center class="half">
<img src="assets/g9.jpg" width="90"/>
<img src="assets/g9_d.png" width="90"/>
<img src="assets/g9_n.jpg" width="90"/>
<img src="assets/g9.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g10.jpg" width="90"/>
<img src="assets/g10_d.png" width="90"/>
<img src="assets/g10_n.jpg" width="90"/>
<img src="assets/g10.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>

<center class="half">
<img src="assets/g11.jpg" width="90"/>
<img src="assets/g11_d.png" width="90"/>
<img src="assets/g11_n.jpg" width="90"/>
<img src="assets/g11.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g12.jpg" width="90"/>
<img src="assets/g12_d.png" width="90"/>
<img src="assets/g12_n.jpg" width="90"/>
<img src="assets/g12.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>

<center class="half">
<img src="assets/g13.jpg" width="90"/>
<img src="assets/g13_d.png" width="90"/>
<img src="assets/g13_n.jpg" width="90"/>
<img src="assets/g13.gif?raw=true" alt="Sublime's custom image" width="90"/>
<img src="assets/g14.jpg" width="90"/>
<img src="assets/g14_d.png" width="90"/>
<img src="assets/g14_n.jpg" width="90"/>
<img src="assets/g14.gif?raw=true" alt="Sublime's custom image" width="90"/>
</center><br>


## News
- **2025-08-28:** updata readme.
