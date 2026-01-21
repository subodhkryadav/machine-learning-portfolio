# 📈 Supervised Learning: Regression Algorithms Portfolio

## 📌 Project Overview
This repository contains professional implementations of **Regression** algorithms designed to predict continuous numerical values. Each project focuses on minimizing residuals and maximizing the variance explained ($R^2$) through advanced optimization and ensemble methods.

---

## 🛠️ Algorithms Implementation

### 1. K-Nearest Neighbors (KNN) Regressor
- **Function:** Predicts values by averaging the targets of the nearest 'k' neighbors.
- **Optimization:** Fine-tuning distance metrics and neighbor counts.

### 2. Support Vector Regression (SVR)
- **Function:** Fits the best line within a specific error margin ($\epsilon$-insensitive tube).
- **Kernels:** Implementation of RBF and Linear kernels for non-linear mapping.


### 3. Decision Tree Regressor
- **Function:** Partitions data into subsets and predicts values based on the average of leaf nodes.

### 4. Random Forest Regressor
- **Function:** An ensemble of multiple regression trees (Bagging) to reduce variance and improve stability.


### 5. AdaBoost Regressor
- **Function:** Combines multiple weak regressors by adjusting weights based on prediction errors.

### 6. Gradient Boosting Regressor
- **Function:** Sequentially adds predictors to an ensemble, each one correcting its predecessor's residuals.


### 7. XGBoost Regressor (with Optuna)
- **Function:** High-performance boosting implementation optimized for speed and accuracy.
- **Optimization:** Automated hyperparameter tuning using **Optuna** for RMSE minimization.


### 8. Linear Regression
- **Function:** The fundamental model that estimates the linear relationship between variables.

---

## 📉 Performance Evaluation
- **R-Squared ($R^2$):** Measures the proportion of variance captured by the model.
- **Mean Squared Error (MSE):** Quantifies the average squared difference between actual and predicted values.
- **Root Mean Squared Error (RMSE):** Error metric in the original units of the target variable.
- **Learning Curves:** Visual diagnosis of Underfitting (High Bias) vs. Overfitting (High Variance).


---

## 🚀 Key Technical Features
- **Hyperparameter Tuning:** Automated search via **Optuna** for advanced models.
- **Feature Engineering:** Handling multi-collinearity and outliers.
- **Scaling:** Implementation of `StandardScaler` for distance-sensitive algorithms.