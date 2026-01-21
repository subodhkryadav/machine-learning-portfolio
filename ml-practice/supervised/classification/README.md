# 🎯 Supervised Learning: Classification Algorithms Portfolio

## 📌 Project Overview
This repository contains industry-standard implementations of various **Classification** algorithms. The projects demonstrate how to handle binary and multi-class problems using a diverse range of models, from probabilistic approaches to advanced boosting techniques.

---

## 🛠️ Algorithms Implementation

### 1. Logistic Regression
- **Function:** Predicts categorical outcomes using the Sigmoid function.
- **Usage:** Baseline binary classification tasks.


### 2. K-Nearest Neighbors (KNN)
- **Function:** A distance-based classifier that labels data based on proximity to neighbors.
- **Optimization:** Hyperparameter tuning for the optimal 'k' value.

### 3. Naive Bayes (GaussianNB)
- **Function:** Based on Bayes' Theorem, assumes feature independence.
- **Use Case:** High-dimensional data like Census and Medical records.

### 4. Support Vector Machine (SVM/SVC)
- **Function:** Finds the optimal hyperplane to maximize the margin between classes.
- **Kernels:** Implementation of Linear and RBF kernels.


### 5. Decision Tree Classifier
- **Function:** Uses a tree structure to split data based on Gini Impurity or Information Gain.

### 6. Random Forest Classifier
- **Function:** An ensemble of decision trees (Bagging) to reduce variance and improve stability.

### 7. AdaBoost (Adaptive Boosting)
- **Function:** Sequentially trains weak learners to correct previous classification errors.

### 8. Gradient Boosting Classifier
- **Function:** Minimizes loss functions iteratively using gradient descent.

### 9. XGBoost Classifier (with Optuna)
- **Function:** State-of-the-art Gradient Boosting implementation.
- **Optimization:** Integrated with **Optuna** for automated Bayesian hyperparameter search.


---

## 📊 Performance Evaluation
- **Accuracy Score:** Percentage of correct predictions.
- **Confusion Matrix:** Breakdown of TP, TN, FP, FN.
- **Precision, Recall, & F1-Score:** Critical for imbalanced datasets.
- **ROC-AUC:** Measuring the model's ability to distinguish between classes.