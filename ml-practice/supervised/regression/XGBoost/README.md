# 🚀 Advanced Regression Projects: XGBoost + Optuna Tuning

## 📌 Project Summary
This repository contains two high-performance regression projects focused on predictive modeling using **XGBoost** and **Optuna**. 
1. **Graduates Admission Prediction**: Estimating admission probability for students.
2. **Boston House Price Prediction**: Real estate valuation based on urban features.

---

## 🧩 Technical Approach: XGBoost & Optuna
In both projects, we moved beyond standard models by implementing **Bayesian Optimization** through **Optuna**. This allowed for:
- Automated search for the best hyperparameters.
- Efficient handling of large feature sets.
- Visualization of the optimization process (Slice plots and trials).



---

## 📊 Project Comparison

| Feature | Graduate Admission | Boston Housing |
| :--- | :--- | :--- |
| **Target Variable** | Chance of Admit (0 to 1) | Median Home Value ($1000s) |
| **Core Algorithm** | XGBoost Regressor | XGBoost Regressor |
| **Optimization** | Optuna (MSE objective) | Optuna (RMSE objective) |
| **Key Driver** | CGPA | RM (Rooms) & LSTAT |

---

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**:
  - `XGBoost`: Gradient boosting framework.
  - `Optuna`: Next-generation hyperparameter optimization.
  - `Scikit-Learn`: For data splitting and metrics.
  - `Pandas/NumPy`: Data manipulation.
  - `Seaborn/Matplotlib`: Statistical visualizations.



---

## 📈 Optimization Insights
By using Optuna, we were able to visualize the "Importance" of each hyperparameter. For both models, parameters like `n_estimators` and `max_depth` were critical in balancing the bias-variance tradeoff, ensuring the models generalize well to new data.

---

## 🚀 How to Run
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install xgboost optuna pandas scikit-learn matplotlib