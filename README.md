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
|                           |   Mean | Std    |
|---------------------------|--------|--------|
| Mean IoU (threshold 0.5)  | 0.6849 | 0.3495 |
| Average Precision         | 0.3723 | 0.4096 |
| Mean Average Precision    | 0.3731 |    -   |



## Some Predicted Image of Validation Dataset

    Image                Ground Truth           Prediction              CAM plot    
**1)**<img src="best_predict_on_val/0.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/0_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/0_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img11.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/0.png_attention.png" alt="CAM_PLOT" width="150"/> 


**2)**<img src="best_predict_on_val/3.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/3_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/3_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img123.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/3.png_attention.png" alt="CAM_PLOT" width="150"/> 


**3)**<img src="best_predict_on_val/45.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/45_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/45_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img146.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/45.png_attention.png" alt="CAM_PLOT" width="150"/> 


**4)**<img src="best_predict_on_val/50.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/50_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/50_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img287.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/50.png_attention.png" alt="CAM_PLOT" width="150"/> 


**5)**<img src="best_predict_on_val/65.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/65_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/65_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img376.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/65.png_attention.png" alt="CAM_PLOT" width="150"/> 


**6)**<img src="best_predict_on_val/71.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/71_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/71_pred.pn](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img430.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/71.png_attention.png" alt="CAM_PLOT" width="150"/> 


**7)**<img src="best_predict_on_val/72.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/72_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/72_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img49.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/72.png_attention.png" alt="CAM_PLOT" width="150"/>


**8)**<img src="best_predict_on_val/140.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/140_ground.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img550.png" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/140.png_attention.png" alt="CAM_PLOT" width="150"/> 


**9)**<img src="best_predict_on_val/183.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/183_ground.png" alt="Ground Truth" width="150"/> <img src="https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img648.png" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/183.png_attention.png" alt="CAM_PLOT" width="150"/> 


**10)**<img src="best_predict_on_val/208.png" alt="OriginalImage" width="150"/> <img src="best_predict_on_val/208_ground.png" alt="Ground Truth" width="150"/> <img src="[best_predict_on_val/208_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img76.png)" alt="Bleeding Prediction" width="150"/> <img src="best_predict_on_val/208.png_attention.png" alt="CAM_PLOT" width="150"/> 



## Some Predicted Images of Test 1 Dataset
    Image                     Prediction                  CAM plot
**1)**<img src="best_predict_on_test1/A0036.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test1/A0036_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0001.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test1/A0036.png_attention.png" alt="CAM_PLOT" width="200"/>


**2)**<img src="best_predict_on_test1/A0037.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test1/A0037_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0012.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test1/A0037.png_attention.png" alt="CAM_PLOT" width="200"/>


**3)**<img src="best_predict_on_test1/A0038.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test1/A0038_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0020.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test1/A0038.png_attention.png" alt="CAM_PLOT" width="200"/>


**4)**<img src="best_predict_on_test1/A0039.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test1/A0039_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0021.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test1/A0039.png_attention.png" alt="CAM_PLOT" width="200"/>


**5)**<img src="best_predict_on_test1/A0047.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test1/A0047_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0045.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test1/A0047.png_attention.png" alt="CAM_PLOT" width="200"/>


## Some Predicted Images of Test 2 Dataset
**1)**<img src="best_predict_on_test2/A0061.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test2/A0061_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0269.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test2/A0061.png_attention.png" alt="CAM_PLOT" width="200"/>


**2)**<img src="best_predict_on_test2/A0173.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test2/A0173_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0355.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test2/A0173.png_attention.png" alt="CAM_PLOT" width="200"/>


**3)**<img src="best_predict_on_test2/A0205.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test2/A0205_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0375.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test2/A0205.png_attention.png" alt="CAM_PLOT" width="200"/>


**4)**<img src="best_predict_on_test2/A0298.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test2/A0298_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0420.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test2/A0298.png_attention.png" alt="CAM_PLOT" width="200"/>


**5)**<img src="best_predict_on_test2/A0283.png" alt="OriginalImage" width="200"/> <img src="[best_predict_on_test2/A0283_pred.png](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0550.png)" alt="Bleeding Prediction" width="200"/> <img src="best_predict_on_test2/A0283.png_attention.png" alt="CAM_PLOT" width="200"/>




## Dataset
To apply the model to a custom dataset, the data tree should be constructed as follows:
``` 
    ├── data
          ├── images
                ├── image_1.png
                ├── image_2.png
                ├── image_n.png
          ├── masks
                ├── image_1.png
                ├── image_2.png
                ├── image_n.png
```
## CSV generation 
```
python data_split_csv.py --dataset your/data/path --size 0.9 
```
## Acknowledgement
The codes are modified from [U-Net](https://github.com/xq141839/DCSAU-Net)
