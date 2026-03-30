**Brain Tumor Classification using Deep Learning**

This project focuses on classifying brain tumor MRI images into multiple categories using deep learning techniques. Both custom CNN and transfer learning models are implemented and compared to identify the best-performing model.

**Objectives**

Classify MRI images into tumor types:
Glioma
Meningioma
Pituitary
No Tumor

Compare performance of:
Custom CNN
Pretrained models (ResNet50, MobileNet, InceptionV3, EfficientNetB0)
Deploy the best model using a Streamlit web application

**Dataset**
Organized into class-wise folders
Total classes: 4
Dataset split:
Training: 1358 images
Validation: 337 images

**Class Distribution**
Glioma: 564
Meningioma: 358
No Tumor: 335
Pituitary: 438

**Model Building**

🔹 Custom CNN
Convolution + Pooling layers
Batch Normalization
Dropout for regularization
Fully connected layers for classification

🔹 Transfer Learning Models
ResNet50
MobileNet
InceptionV3
EfficientNetB0

**Callbacks Used**
EarlyStopping (to prevent overfitting)
ModelCheckpoint (to save best model)

**Model Evaluation**

Metrics used:
Accuracy
Precision
Recall
F1-score
Confusion Matrix

**Streamlit Deployment**

Features:
Upload MRI image
Predict tumor type
Display confidence score
Show class probabilities
