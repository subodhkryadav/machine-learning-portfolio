# 🧬 Dimensionality Reduction: PCA Portfolio

## 📌 Project Overview
This repository showcases the implementation of **Principal Component Analysis (PCA)** for both theoretical understanding and practical application. PCA is a powerful unsupervised technique used for feature extraction, noise reduction, and data visualization.

---

## 🛠️ Algorithms & Techniques

### 1. Principal Component Analysis (PCA)
- **Objective**: Reduce the dimensionality of the dataset while preserving the most important information (variance).
- **Scaling**: All features are standardized to have a mean of 0 and variance of 1 before applying PCA.
- **Selection**: Using **Screen Plots** and **Cumulative Explained Variance** to select the optimal number of components.



### 2. Decision Tree Integration
- Combined PCA-transformed features with a **Decision Tree Classifier** to demonstrate how dimensionality reduction can simplify model training without significant loss in accuracy.

---

## 📊 Evaluation Metrics
- **Explained Variance Ratio (EVR)**: To measure the information retained by each component.
- **Cumulative Variance**: To determine the threshold for dimensionality reduction.
- **Classification Accuracy**: To validate the performance of the model on reduced data.

---

## ⚙️ Tech Stack
- **Language**: Python
- **Libraries**: Scikit-Learn, Pandas, NumPy, Matplotlib.

---

## 🚀 How to Navigate
- **PCA.ipynb**: Best for understanding the math (Covariance, Eigenvectors).
- **PCA1.ipynb**: Best for seeing PCA in a real-world classification pipeline.