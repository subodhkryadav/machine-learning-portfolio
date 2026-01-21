# 🚀 Classification Suite: Wine Quality & College Placement (XGBoost + Optuna)

## 📌 Project Summary
This repository contains two advanced classification projects focusing on high-performance modeling using **XGBoost** and **Optuna**.
1. **Wine Quality Prediction**: A multi-class classification problem.
2. **College Placement Prediction**: A binary classification problem comparing multiple models.

---

## 🧩 Technical Approach: XGBoost with Optuna
In these projects, we utilize **Optuna** to automate hyperparameter tuning. This approach is superior to manual tuning as it uses a "Trial" based system to find the global optimum for the XGBoost model.



### ⚙️ Optimization Features:
- **Bayesian Optimization**: Faster search than GridSearch.
- **Metric Tracking**: Monitoring Accuracy and AUC-ROC across trials.
- **Visualization**: Using Optuna's plotting tools to see parameter influence.

---

## 📊 Project Comparison

| Metric | Wine Quality Prediction | College Placement |
| :--- | :--- | :--- |
| **Problem Type** | Multi-Class Classification | Binary Classification |
| **Primary Model** | XGBoost Classifier | XGBoost vs. Logistic Regression |
| **Key Optimizer** | Optuna | Optuna |
| **Strongest Feature** | Alcohol Content | CGPA |

---

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**:
  - `XGBoost`: High-performance gradient boosting.
  - `Optuna`: For automated hyperparameter tuning.
  - `YData-Profiling`: For automated EDA.
  - `Scikit-Learn`: Preprocessing and metrics (Accuracy, F1-Score, AUC-ROC).
  - `Seaborn/Matplotlib`: Data visualization.



---

## 📈 Performance Highlights
For the **College Placement** project, a comparison was made between Logistic Regression and XGBoost. The results showed that the boosted trees (XGBoost) could better identify edge-case students who had lower CGPA but high internship experience.

For **Wine Quality**, the model successfully grouped wines into quality tiers, effectively handling the chemical variance across 1,500+ samples.

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install xgboost optuna ydata-profiling pandas scikit-learn