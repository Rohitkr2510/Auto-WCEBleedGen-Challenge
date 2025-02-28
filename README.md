# Auto-WCEBleedGen Challenge
Automatic Classification, Segmentation and Detection of Bleeding and Non-Bleeding Frames in a Wireless Capsule Endoscopy Images.

# Team name : The Coders


**Code and Model Location**
- The code for training the model can be found in the 'code' folder of this repository.
- The trained model itself is available in the same 'model' folder.

**Testing Results**
- Results for the test dataset are located in the 'result_excel'and 'result' folder.

## Achieved Evaluation Metrics 

### Classification Metrics

We have evaluated the classification model using the following metrics on the validation dataset:
Metric                 | Value
---------------------- | -------------
Accuracy               | 0.9866412281990051
Recall                 | 0.9821428656578064
F1 Score               | 0.9860557317733765

### Segmentation Metrics
|       Metric              |  value | 
|---------------------------|--------|
| IoU                       | 0.3049 |  
| Average Precision         | 0.3523 |  
| Mean Average Precision    | 0.3331 |    -   



## Some Predicted Image of Validation Dataset

    Image                Mask                 Prediction              CAM plot    
**1)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img11.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/11.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img11.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/11.png_attention.png" alt="CAM_PLOT" width="150"/> 


**2)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img123.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/123.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img123.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/123.png_attention.png" alt="CAM_PLOT" width="150"/> 


**3)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img146.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/146.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img146.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/146.png_attention.png" alt="CAM_PLOT" width="150"/> 


**4)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img287.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/287.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img287.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/287.png_attention.png" alt="CAM_PLOT" width="150"/> 


**5)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img376.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/376.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img376.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/376.png_attention.png" alt="CAM_PLOT" width="150"/> 


**6)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img430.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/430.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img430.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/430.png_attention.png" alt="CAM_PLOT" width="150"/> 


**7)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img49.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/49.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img49.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/49.png_attention.png" alt="CAM_PLOT" width="150"/>


**8)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img550.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/550.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img550.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/550.png_attention.png" alt="CAM_PLOT" width="150"/> 


**9)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img648.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/648.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img648.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/648.png_attention.png" alt="CAM_PLOT" width="150"/> 


**10)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/img76.png" alt="OriginalImage" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/val/masks/76.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img76.png" alt="Bleeding Prediction" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/val/76.png_attention.png" alt="CAM_PLOT" width="150"/> 



## Some Predicted Images of Test 1 Dataset
    Image                     Prediction                  CAM plot
**1)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test1/1.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0001.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test1/A0001.png_attention.png" alt="CAM_PLOT" width="200"/>


**2)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test1/12.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0012.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test1/A0012.png_attention.png" alt="CAM_PLOT" width="200"/>


**3)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test1/20.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0020.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test1/A0020.png_attention.png" alt="CAM_PLOT" width="200"/>


**4)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test1/21.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0021.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test1/A0021.png_attention.png" alt="CAM_PLOT" width="200"/>


**5)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test1/45.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0045.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test1/A0045.png_attention.png" alt="CAM_PLOT" width="200"/>


## Some Predicted Images of Test 2 Dataset
**1)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test2/A0269.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0269.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test2/A0269.png_attention.png" alt="CAM_PLOT" width="200"/>


**2)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test2/A0355.png" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0355.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test2/A0355.png_attention.png" alt="CAM_PLOT" width="200"/>


**3)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test2/A0375.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0375.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test2/A0375.png_attention.png" alt="CAM_PLOT" width="200"/>


**4)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test2/A0420.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0420.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test2/A0420.png_attention.png" alt="CAM_PLOT" width="200"/>


**5)**<img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/test2/A0550.png" alt="OriginalImage" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0550.png" alt="Bleeding Prediction" width="200"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/assets/Cam_Plot/test2/A0550.png_attention.png" alt="CAM_PLOT" width="200"/>


## ACHIEVED RANK 11th IN CAPSULE VISION CHALLENGE 2024


## Acknowledgement
As participants in the Auto-WCEBleedGen Version V1 Challenge, we fully comply with
the competition rules as outlined in [1] and the challenge website. Our methods have used
the training and test data sets provided in the official release in [2] and [3] to report the
results of the challenge.

## Reference
1) @article{hub2024auto,
  title={Auto-WCEBleedGen Version V1 and V2: Challenge, Datasets and Evaluation},
  author={Handa, Palak and Nautiyal, Divyansh and Chhabra, Deepti and Dhir, Manas and Saini, Anushka and Jha, Shreshtha and Mangotra, Harshita and Pandey, Nishu and Thakur, Advika and others},
  journal={Authorea Preprints},
  year={2024},
  publisher={Authorea},
 doi          = {10.22541/essoar.171007121.19572474/v1}
}
%train
2) @misc{palakbleedingtrain,
  author       = {Palak and
                  Harshita Mangotra and
                  Nautiyal, Divyansh and
                  Jyoti Dhatarwal and
                  Nidhi Gooel},
  title        = {WCEbleedGen:  A wireless capsule endoscopy dataset
                   containing bleeding and non-bleeding frames
                  },
  month        = nov,
  year         = 2023,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.10156571},
  url          = {https://doi.org/10.5281/zenodo.10156571}
}
%test
3) @misc{palakbleedingtest,
  author       = {Handa, Palak and
                  Pandey, Nishu and
                  Nautiyal, Divyansh and
                  Goel, Nidhi and
                  Gunjan, Deepak},
  title        = {AutoWCEBleedGen-Test Dataset (Improved)},
  month        = feb,
  year         = 2024,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.10642779},
  url          = {https://doi.org/10.5281/zenodo.10642779}
}
4) @inproceedings{ronneberger2015unet,
  author    = {Olaf Ronneberger and Philipp Fischer and Thomas Brox},
  title     = {U-net: Convolutional networks for biomedical image segmentation},
  booktitle = {Medical Image Computing and Computer-Assisted Intervention--MICCAI 2015: 18th International Conference, Munich, Germany, October 5-9, 2015, Proceedings, Part III},
  year      = {2015},
  publisher = {Springer International Publishing}
}

5) @article{abhishek2022resnet18,
  author    = {Abhishek and Allena Venkata Sai and Dr. Venkateswara Rao Gurrala and Dr. Laxman Sahoo},
  title     = {Resnet18 model with sequential layer for computing accuracy on image classification dataset},
  journal   = {International Journal of Creative Research Thoughts (IJCRT)},
  year      = {2022},
}

6) @article{kang2023bgf,
  author    = {Kang, M. and Ting, C. M. and Ting, F. F. and Phan, R. C. W.},
  title     = {Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection},
  journal   = {arXiv preprint arXiv:2309.12585},
  year      = {2023},
  url       = {https://arxiv.org/abs/2309.12585}
}


