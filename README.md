# <p align=center> [IEEE Access 2020] Low-Light Image Enhancement With Regularized Illumination Optimization and Deep Noise Suppression</p>

<div align="center">
 
[![Paper](https://img.shields.io/badge/LLIE-Paper-red.svg)](https://ieeexplore.ieee.org/abstract/document/9163095)

</div>

---
>**Low-Light Image Enhancement With Regularized Illumination Optimization and Deep Noise Suppression**<br>
[Yu Guo](https://scholar.google.com/citations?user=klYz-acAAAAJ&hl=zh-CN)<sup>†</sup>, [Yuxu Lu]((https://scholar.google.com.hk/citations?user=XXge2_0AAAAJ&hl=zh-CN))<sup>†</sup>, [Ryan Wen Liu](http://mipc.whut.edu.cn/index.html)<sup>* </sup>, Meifang Yang, Kwok Tai Chui*<sup>* </sup> <br>
(† Co-first Author, * Corresponding Author)<br>
>IEEE Access

> **Abstract:** *Maritime images captured under low-light imaging condition easily suffer from low visibility and unexpected noise, leading to negative effects on maritime traffic supervision and management. To promote imaging performance, it is necessary to restore the important visual information from degraded low-light images. In this article, we propose to enhance the low-light images through regularized illumination optimization and deep noise suppression. In particular, a hybrid regularized variational model, which combines L0-norm gradient sparsity prior with structure-aware regularization, is presented to refine the coarse illumination map originally estimated using Max-RGB. The adaptive gamma correction method is then introduced to adjust the refined illumination map. Based on the assumption of Retinex theory, a guided filter-based detail boosting method is introduced to optimize the reflection map. The adjusted illumination and optimized reflection maps are finally combined to generate the enhanced maritime images. To suppress the effect of unwanted noise on imaging performance, a deep learning-based blind denoising framework is further introduced to promote the visual quality of enhanced image. In particular, this framework is composed of two sub-networks, i.e., E-Net and D-Net adopted for noise level estimation and non-blind noise reduction, respectively. The main benefit of our image enhancement method is that it takes full advantage of the regularized illumination optimization and deep blind denoising. Comprehensive experiments have been conducted on both synthetic and realistic maritime images to compare our proposed method with several state-of-the-art imaging methods. Experimental results have illustrated its superior performance in terms of both quantitative and qualitative evaluations.*
---

## Requirement
* __Python__ == 3.7
* __Matlab__ == 2019a
* __Pytorch__ == 1.1.0
* __MATLAB Engine API for python__

## Flowchart of Our Proposed Method
In the first step, a hybrid regularized variational model is proposed to refine the coarse illumination map originally estimated using Max-RGB. In the second step, an adaptive gamma correction method and a guided filter-based detail boosting method are adopted to optimize the reflection map. The refined illumination and optimized reflection maps are combined to generate the final enhanced images. As a post-processing step, the blind denoising framework is introduced to reduce the unwanted noise to further improve visual image quality.
![Fig2](https://user-images.githubusercontent.com/48637474/135098754-9353c72c-02c2-4c83-b06f-b9b3979d5fee.jpg)
**FIGURE 2. Flowchart of our proposed method for enhancing low-light maritime images.**

![Fig3](https://user-images.githubusercontent.com/48637474/135105375-a44444fa-159d-4bc7-8b10-0aa7ec377be6.jpg)
**FIGURE 4. The architecture of blind denoising network used in this work.**

## Test
* Put the low-light image in the `image` folder
* Run `main.py`. 
* The enhancement result will be saved in the `Result` folder.

## Citation

```
@article{guo2020low,
  title={Low-light image enhancement with regularized illumination optimization and deep noise suppression},
  author={Guo, Yu and Lu, Yuxu and Liu, Ryan Wen and Yang, Meifang and Chui, Kwok Tai},
  journal={IEEE Access},
  volume={8},
  pages={145297--145315},
  year={2020}
}
```

#### If you have any questions, please get in touch with me (guoyu65896@gmail.com).
