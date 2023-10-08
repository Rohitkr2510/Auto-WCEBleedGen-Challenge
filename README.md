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
Accuracy               | 93.32
Recall - Bleeding      | 87.78
Recall - Non-Bleeding  | 98.85
F1 Score               | 92.92

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
![img- (6)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/627f345e-9f88-453f-9f55-8fabbb82280d)
<br> Bleeding Frame
<br> tensor([[131.00000, 170.00000, 203.00000, 215.00000,   0.38539,   0.00000]])
<br> tensor([[131.00000, 148.00000, 204.00000, 216.00000,   0.27617,   0.00000]])

### Image-2 ID: img- (12)
![img- (12)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/fcf5e84a-7c90-4ee6-b7b4-13cb748395f6)
<br> Bleeding Frame
<br> tensor([[ 75.00000, 156.00000, 178.00000, 220.00000,   0.56155,   0.00000]])

### Image-3 ID: img- (77)
![img- (77)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/715b16c2-7d5c-40cf-a04a-4dd77e4e1e44)
<br> Bleeding Frame
<br> tensor([[145.00000,  22.00000, 193.00000,  86.00000,   0.51087,   0.00000]])

### Image-4 ID: img- (215)
![img- (215)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/b93d1f0c-d556-44f3-84d8-6508849e37e0)
<br> Bleeding Frame
<br> tensor([[110.00000, 132.00000, 205.00000, 158.00000,   0.69729,   0.00000]])

### Image-5 ID: img- (391)
![img- (391)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/e1046a41-221a-468f-a323-c85fb13de09e)
<br> Bleeding Frame
<br> tensor([[  9.00000,  15.00000, 222.00000, 224.00000,   0.89529,   0.00000]])

### Image-6 ID: img- (676)
![img- (676)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/80f27599-6055-4838-8681-256bb17ec2c1)
<br> Bleeding Frame
<br> tensor([[ 67.00000,  33.00000, 150.00000, 123.00000,   0.72962,   0.00000]])

### Image-7 ID: img- (954)
![img- (954)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/3ea3ad3b-4d09-4567-8561-c47cfee4c86b)
<br> Bleeding Frame
<br> tensor([[ 82.00000,  88.00000, 165.00000, 154.00000,   0.83264,   0.00000]])

### Image-8 ID: img- (1078)
![img- (1078)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/4d6b47b3-078d-41f9-af82-f82cc98d1f51)
<br> Bleeding Frame
<br> tensor([[ 46.00000,  79.00000,  74.00000, 127.00000,   0.68358,   0.00000]])
<br> tensor([[ 83.00000, 144.00000, 160.00000, 192.00000,   0.49040,   0.00000]])
<br> tensor([[135.00000,  41.00000, 176.00000, 105.00000,   0.27353,   0.00000]])

### Image-9 ID: img- (1146)
![img- (1146)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/4fa9bb6e-d54d-4092-bcff-0ac6dcc2bf8b)
<br> Bleeding Frame
<br> tensor([[  1.00000,  43.00000, 119.00000, 161.00000,   0.93680,   0.00000]])

### Image-10 ID: img- (1213)
![img- (1213)](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/0808bcd9-ef80-407e-8b0c-3b077d57a05e)
<br> Bleeding Frame
<br> tensor([[10.00000,  0.00000, 68.00000, 91.00000,  0.84781,  0.00000]])


# Testing Dataset Results
## Classification and Detection Visualizations
We have also tested the model on two separate testing datasets (Test Dataset 1 and Test Dataset 2). Here are screenshots/pictures of the top 5 images selected from each testing dataset, showing both the classification results and detection results with bounding boxes and confidence levels:
Format (Bounded Boxes Confidence Label)

## From Test_Dataset_1

### Image-1 ID: A0005
![A0005](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/18d99bc7-799a-44e1-a2a7-f08f6e4b09ad)
<br> Bleeding Frame
<br> tensor([[ 72.00000, 134.00000,  94.00000, 157.00000,   0.37013,   0.00000]])

### Image-2 ID: A0025
![A0025](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/d0c9ae00-05a0-4e5b-b080-bfe70458bc29)
<br> Bleeding Frame
<br> tensor([[ 65.00000,   1.00000, 127.00000,  85.00000,   0.35578,   0.00000]])

### Image-3 ID: A0026
![A0026](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/f2920176-89f9-48ac-8283-8349e7ac184b)
<br> Bleeding Frame
<br> tensor([[ 82.00000,  14.00000, 131.00000,  94.00000,   0.42494,   0.00000]])

### Image-4 ID: A0037
![A0037](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/cee29a6f-ec1c-4052-b587-3c71e9f0922b)
<br> Bleeding Frame
<br> tensor([[ 96.00000,   3.00000, 222.00000,  80.00000,   0.34570,   0.00000]])

### Image-5 ID: A0046
![A0046](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/c12a026a-3a06-4391-9b7a-28703bd04b72)
<br> Bleeding Frame
<br> tensor([[ 43.00000,  90.00000, 132.00000, 157.00000,   0.38476,   0.00000]])

## From Test_Dataset_2

### Image-1 ID: A0141
![A0141](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/6ba288e3-9f12-48b5-a864-ab57b19b8fa0)
<br> Bleeding Frame
<br> tensor([[ 34.00000,   2.00000, 204.00000, 222.00000,   0.70168,   0.00000]])

### Image-2 ID: A0375
![A0375](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/5afcfdef-0a1b-44f0-a9c3-746e4a54a60b)
<br> Bleeding Frame
<br> tensor([[ 72.00000,   0.00000, 127.00000,  68.00000,   0.78682,   0.00000]])

### Image-3 ID: A0399
![A0399](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/fac89aaf-6289-414d-9b49-12727c494d86)
<br> Bleeding Frame
<br> tensor([[120.00000,  33.00000, 156.00000, 119.00000,   0.40065,   0.00000]])
<br> tensor([[ 51.00000,  18.00000, 157.00000, 162.00000,   0.25606,   0.00000]])

### Image-4 ID: A0467
![A0467](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/5d5e2513-2429-49ab-a6da-4ef39123f372)
<br> Bleeding Frame
<br> tensor([[ 87.00000, 132.00000, 124.00000, 182.00000,   0.45395,   0.00000]])
<br> tensor([[118.00000, 154.00000, 172.00000, 208.00000,   0.39441,   0.00000]])
<br> tensor([[ 80.00000, 133.00000, 174.00000, 215.00000,   0.27501,   0.00000]])

### Image-5 ID: A0484
![A0484](https://github.com/Shivam-027/Auto-WCEBleedGen-Challenge/assets/109764676/e00bf7ce-2988-48a1-b878-fc1162b0623e)
<br> Bleeding Frame
<br> tensor([[111.00000,  69.00000, 132.00000,  92.00000,   0.48386,   0.00000]])
