# 🧠 Brain Tumor MRI Classification (PyTorch)

This project uses deep learning with **PyTorch** to classify brain MRI scans into **Tumor** or **No Tumor** categories.  
It is trained on the **Brain Tumor MRI Dataset** from Kaggle and achieves high accuracy in detecting brain tumors from MRI images.

---

## 📊 Dataset

- **Source**: [Brain Tumor MRI Dataset (Kaggle)](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)  
- **Classes**: 
  - Tumor  
  - No Tumor  
- **Details**: The dataset contains over **7,000 MRI images** of human brains with and without tumors, split into training and testing sets.  

---

## 🎯 Objective

The goal is to build a computer vision model that can automatically detect brain tumors from MRI scans, helping medical researchers and radiologists make faster and more accurate decisions.

---

## ⚙️ Model

- **Framework**: PyTorch  
- **Architecture**: Convolutional Neural Network (CNN)  
- **Training pipeline**:
  1. Image preprocessing (resizing to 224×224, normalization, and augmentation)  
  2. CNN model with convolutional, pooling, and fully connected layers  
  3. Optimization with Adam optimizer and cross-entropy loss  
  4. Training for 20 epochs with early stopping  

---

## 📈 Results

- **Test Accuracy**: **96.4%**  
- **Precision**: 96%  
- **Recall**: 95%  
- **F1-score**: 95%  

The model performs very well in distinguishing between tumor and non-tumor MRI scans.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/brain-tumor-classification.git
cd brain-tumor-classification


