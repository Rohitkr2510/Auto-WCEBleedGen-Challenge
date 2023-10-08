# Auto-WCEBleedGen-Challenge
This repository contains our submission for the Auto-WCEBleedGen Challenge. The primary objective of this challenge was to develop a classification and detection model capable of distinguishing between bleeding and non-bleeding frames in wireless capsule endoscopy (WCE) images. In this README, we provide an overview of the project, the achieved evaluation metrics, and visualizations of the model's performance on validation and testing datasets.

## Team Name: Techy Bots

## Model Used
We employed the YOLOv8 model architecture for this task. We merged both the bleeding and non-bleeding images. The bleeding images follow the naming convention 'img- (n)', while the non-bleeding images are labeled as 'imgnb- (n)', where '(n)' represents a numerical identifier.

**Code and Model Location**
- The code for training the model can be found in the 'MODEL' folder of this repository.
- The trained model itself is available in the same 'MODEL' folder.

**Testing Results**
- Results for the test dataset are located in the 'RESULT' folder.

### Key Highlights
**Classification and Detection:** Our model not only classifies images but also detects bleeding regions with bounding boxes and confidence levels.
**Data Merging:** We merged bleeding and non-bleeding images during training to improve model generalization.

# Evaluation Metrics
## Classification Metrics
We have evaluated the classification model using the following metrics on the validation dataset:
Metric                 | Value
---------------------- | -------------
Accuracy               | 0.9866412281990051
Recall                 | 0.9821428656578064
F1 Score               | 0.9860557317733765

## Detection Metrics
The detection model's performance on the validation dataset is assessed using the following metrics:
Metric                            | Value
--------------------------------- | -------------
Average Precision - Bleeding      | 77.39
Average Precision - Non-Bleeding  | 33.33
Mean Average Precision            | 55.36
Intersection over Union           | 16.93

![image](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/bf0538cf-e05c-40d6-9eb4-1bfc6e0dfc4d)

# Validation Dataset Results
## Classification and Detection Visualizations
Here are screenshots/pictures of the top 10 images selected from the validation dataset, showcasing both the classification results and detection results with bounding boxes and confidence levels:
Format (Bounded Boxes Confidence Label)

### Image-1 ID: img- (6)
![img- (11)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img11.png)
<br> Bleeding Frame
<br> tensor([[131.00000, 170.00000, 203.00000, 215.00000,   0.38539,   0.00000]])
<br> tensor([[131.00000, 148.00000, 204.00000, 216.00000,   0.27617,   0.00000]])

### Image-2 ID: img- (12)
![img- (123)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img123.png)
<br> Bleeding Frame
<br> tensor([[ 75.00000, 156.00000, 178.00000, 220.00000,   0.56155,   0.00000]])

### Image-3 ID: img- (77)
![img- (146)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img146.png)
<br> Bleeding Frame
<br> tensor([[145.00000,  22.00000, 193.00000,  86.00000,   0.51087,   0.00000]])

### Image-4 ID: img- (215)
![img- (287)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img287.png)
<br> Bleeding Frame
<br> tensor([[110.00000, 132.00000, 205.00000, 158.00000,   0.69729,   0.00000]])

### Image-5 ID: img- (391)
![img- (376)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img376.png)
<br> Bleeding Frame
<br> tensor([[  9.00000,  15.00000, 222.00000, 224.00000,   0.89529,   0.00000]])

### Image-6 ID: img- (676)
![img- (430)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img430.png)
<br> Bleeding Frame
<br> tensor([[ 67.00000,  33.00000, 150.00000, 123.00000,   0.72962,   0.00000]])

### Image-7 ID: img- (954)
![img- (49)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img49.png)
<br> Bleeding Frame
<br> tensor([[ 82.00000,  88.00000, 165.00000, 154.00000,   0.83264,   0.00000]])

### Image-8 ID: img- (1078)
![img- (550)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img550.png)
<br> Bleeding Frame
<br> tensor([[ 46.00000,  79.00000,  74.00000, 127.00000,   0.68358,   0.00000]])
<br> tensor([[ 83.00000, 144.00000, 160.00000, 192.00000,   0.49040,   0.00000]])
<br> tensor([[135.00000,  41.00000, 176.00000, 105.00000,   0.27353,   0.00000]])

### Image-9 ID: img- (1146)
![img- (648)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img648.png)
<br> Bleeding Frame
<br> tensor([[  1.00000,  43.00000, 119.00000, 161.00000,   0.93680,   0.00000]])

### Image-10 ID: img- (1213)
![img- (76)](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_10_val_image/img76.png)
<br> Bleeding Frame
<br> tensor([[10.00000,  0.00000, 68.00000, 91.00000,  0.84781,  0.00000]])


# Testing Dataset Results
## Classification and Detection Visualizations
We have also tested the model on two separate testing datasets (Test Dataset 1 and Test Dataset 2). Here are screenshots/pictures of the top 5 images selected from each testing dataset, showing both the classification results and detection results with bounding boxes and confidence levels:
Format (Bounded Boxes Confidence Label)

## From Test_Dataset_1

### Image-1 ID: A0005
![A0001](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0001.png)
<br> Bleeding Frame
<br> tensor([[ 72.00000, 134.00000,  94.00000, 157.00000,   0.37013,   0.00000]])

### Image-2 ID: A0025
![A0012](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0012.png)
<br> Bleeding Frame
<br> tensor([[ 65.00000,   1.00000, 127.00000,  85.00000,   0.35578,   0.00000]])

### Image-3 ID: A0026
![A0020](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0020.png)
<br> Bleeding Frame
<br> tensor([[ 82.00000,  14.00000, 131.00000,  94.00000,   0.42494,   0.00000]])

### Image-4 ID: A0037
![A0021](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0021.png)
<br> Bleeding Frame
<br> tensor([[ 96.00000,   3.00000, 222.00000,  80.00000,   0.34570,   0.00000]])

### Image-5 ID: A0046
![A0045](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test1_images/A0045.png)
<br> Bleeding Frame
<br> tensor([[ 43.00000,  90.00000, 132.00000, 157.00000,   0.38476,   0.00000]])

## From Test_Dataset_2

### Image-1 ID: A0141
![A0269](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0269.png)
<br> Bleeding Frame
<br> tensor([[ 34.00000,   2.00000, 204.00000, 222.00000,   0.70168,   0.00000]])

### Image-2 ID: A0375
![A0355](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0355.png)
<br> Bleeding Frame
<br> tensor([[ 72.00000,   0.00000, 127.00000,  68.00000,   0.78682,   0.00000]])

### Image-3 ID: A0399
![A0375](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0375.png)
<br> Bleeding Frame
<br> tensor([[120.00000,  33.00000, 156.00000, 119.00000,   0.40065,   0.00000]])
<br> tensor([[ 51.00000,  18.00000, 157.00000, 162.00000,   0.25606,   0.00000]])

### Image-4 ID: A0467
![A0420](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0420.png)
<br> Bleeding Frame
<br> tensor([[ 87.00000, 132.00000, 124.00000, 182.00000,   0.45395,   0.00000]])
<br> tensor([[118.00000, 154.00000, 172.00000, 208.00000,   0.39441,   0.00000]])
<br> tensor([[ 80.00000, 133.00000, 174.00000, 215.00000,   0.27501,   0.00000]])

### Image-5 ID: A0484
![A0550](https://github.com/Rohitkr2510/Auto-WCEBleedGen-Challenge/blob/main/results/best_5_test2_images/A0550.png)
<br> Bleeding Frame
<br> tensor([[111.00000,  69.00000, 132.00000,  92.00000,   0.48386,   0.00000]])
