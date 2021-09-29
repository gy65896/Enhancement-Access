# Low-Light Image Enhancement With Regularized Illumination Optimization and Deep Noise Suppression 
  
[**[paper]**](https://ieeexplore.ieee.org/abstract/document/9163095/)

## 1. Requirement ##
* __Python__ == 3.7
* __Matlab__ == 2019a
* __Pytorch__ == 1.1.0

## 2. Abstract
Maritime images captured under low-light imaging condition easily suffer from low visibility and unexpected noise, leading to negative effects on maritime traffic supervision and management. To promote imaging performance, it is necessary to restore the important visual information from degraded low-light images. In this article, we propose to enhance the low-light images through regularized illumination optimization and deep noise suppression. In particular, a hybrid regularized variational model, which combines L0-norm gradient sparsity prior with structure-aware regularization, is presented to refine the coarse illumination map originally estimated using Max-RGB. The adaptive gamma correction method is then introduced to adjust the refined illumination map. Based on the assumption of Retinex theory, a guided filter-based detail boosting method is introduced to optimize the reflection map. The adjusted illumination and optimized reflection maps are finally combined to generate the enhanced maritime images. To suppress the effect of unwanted noise on imaging performance, a deep learning-based blind denoising framework is further introduced to promote the visual quality of enhanced image. In particular, this framework is composed of two sub-networks, i.e., E-Net and D-Net adopted for noise level estimation and non-blind noise reduction, respectively. The main benefit of our image enhancement method is that it takes full advantage of the regularized illumination optimization and deep blind denoising. Comprehensive experiments have been conducted on both synthetic and realistic maritime images to compare our proposed method with several state-of-the-art imaging methods. Experimental results have illustrated its superior performance in terms of both quantitative and qualitative evaluations.

## 3. Flowchart of Our Proposed Method
In the first step, a hybrid regularized variational model is proposed to refine the coarse illumination map originally estimated using Max-RGB. In the second step, an adaptive gamma correction method and a guided filter-based detail boosting method are adopted to optimize the reflection map. The refined illumination and optimized reflection maps are combined to generate the final enhanced images. As a post-processing step, the blind denoising framework is introduced to reduce the unwanted noise to further improve visual image quality.
![Fig2](https://user-images.githubusercontent.com/48637474/135098754-9353c72c-02c2-4c83-b06f-b9b3979d5fee.jpg)
**FIGURE 2. Flowchart of our proposed method for enhancing low-light maritime images.**

![Fig3](https://user-images.githubusercontent.com/48637474/135105375-a44444fa-159d-4bc7-8b10-0aa7ec377be6.jpg)
**FIGURE 4. The architecture of blind denoising network used in this work.**

## 4. Testing
* Put the low-light image in the "image" folder
* Run "main.py". 
* The enhancement result will be saved in the "Result" folder.

## 5. Citation

```
\bibitem{guo2020low} 
Y. Guo, Y. Lu, R. W. Liu, M. Yang, and K. T. Chui, ``Low-light image enhancement with regularized illumination optimization and deep noise suppression,'' \emph{IEEE Access}, vol. 8, pp. 145297-145315, Aug. 2020.
```

```
@article{guo2020low,
  title={Low-Light Maritime Image Enhancement with Regularized Illumination Optimization and Deep Noise Suppression},
  author={Guo, Yu and Lu, Yuxu and Liu, Ryan Wen and Yang, Meifang and Chui, Kwok Tai},
  journal={arXiv preprint arXiv:2008.03765},
  year={2020}
}
```
