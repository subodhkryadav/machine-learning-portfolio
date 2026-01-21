# 🤖 Machine Learning Practice: Comprehensive Portfolio

## 📌 Overview
This repository is a complete end-to-end collection of Machine Learning implementations. It covers the two major pillars of ML: **Supervised Learning** (Predictive Modeling) and **Unsupervised Learning** (Pattern Discovery). The projects demonstrate data preprocessing, feature engineering, automated hyperparameter tuning, and model evaluation.

---

## 🎯 1. Supervised Learning Module
This module is divided into Classification and Regression tasks, focusing on labeled data.

### ✅ Classification (9 Algorithms)
*Focus: Predicting discrete categories.*
- **Algorithms:** Logistic Regression, KNN, Naive Bayes, SVM, Decision Tree, Random Forest, AdaBoost, Gradient Boosting, and **XGBoost (Optuna Optimized)**.
- **Key Metrics:** Accuracy, Confusion Matrix, ROC-AUC.


### ✅ Regression (8 Algorithms)
*Focus: Predicting continuous numerical values.*
- **Algorithms:** Linear Regression, KNN Regressor, SVR, Decision Tree, Random Forest, AdaBoost, Gradient Boosting, and **XGBoost Regressor**.
- **Key Metrics:** R-Squared ($R^2$), MSE, RMSE.


---

## 🔍 2. Unsupervised Learning Module
This module focuses on finding hidden structures and reducing complexity in unlabeled data.

### ✅ Clustering Techniques
- **K-Means:** Customer segmentation using the Elbow Method and WCSS.
- **DBSCAN:** Density-based clustering for noise detection and arbitrary shapes.
- **Hierarchical Clustering:** Agglomerative approach using Dendrograms for species segmentation.


### ✅ Dimensionality Reduction
- **Principal Component Analysis (PCA):** Reducing high-dimensional data (like the Glass dataset) while preserving maximum variance. Used for noise reduction and visualization.


---

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Core Libraries:** Scikit-Learn, XGBoost, Pandas, NumPy.
- **Optimization:** **Optuna** (Automated Hyperparameter Tuning).
- **Visualization:** Matplotlib, Seaborn, Scipy (Dendrograms).
- **EDA:** YData-Profiling.

---

## 📂 Folder Structure
- `/Supervised_Learning`: Contains Classification and Regression notebooks.
- `/Unsupervised_Learning`: Contains Clustering (K-Means, DBSCAN, Hierarchical) and PCA notebooks.

---

## 🚀 How to Use
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt` (or install manually: `scikit-learn xgboost optuna pandas seaborn`).
3. Open any Jupyter Notebook to see the step-by-step implementation from EDA to Prediction.