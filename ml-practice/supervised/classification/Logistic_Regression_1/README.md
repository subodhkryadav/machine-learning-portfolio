# ❤️ Heart Disease Prediction using Logistic Regression

## 📌 Project Description
This project focuses on the medical domain, specifically predicting the presence of **Heart Disease** in patients. By using **Logistic Regression**, we analyze various physiological factors like cholesterol levels, chest pain type, and maximum heart rate to determine the risk of cardiovascular illness.

---

## 🧩 The Importance
Early detection of heart conditions can save lives. This machine learning approach provides a reliable way to assist healthcare professionals in identifying high-risk patients based on diagnostic data.

---

## 📊 Dataset Overview
The dataset contains information from patients undergoing cardiovascular examinations. It is a highly balanced dataset with a mix of categorical and continuous variables.



### 📐 Key Metrics
- **Observations:** 1025
- **Diagnostic Features:** 13
- **Objective:** Binary Classification (Target 0 or 1)

---

## 🧬 Feature Breakdown

| Feature | Description |
| :--- | :--- |
| **Age / Sex** | Demographic information. |
| **Chest Pain (CP)** | Type of chest pain categorized from 0 to 3. |
| **Thalach** | The highest heart rate achieved during stress testing. |
| **Trestbps** | Resting blood pressure levels. |
| **Oldpeak** | ST depression level, an important indicator of heart stress. |
| **Target** | **1** indicates Heart Disease, **0** indicates a Healthy Heart. |

---

## 🛠️ Technology Stack
- **Python**: Core programming language.
- **Pandas & NumPy**: Data cleaning and matrix operations.
- **Scikit-Learn**: Implementing the Logistic Regression model and evaluation metrics.
- **Matplotlib & Seaborn**: Creating insightful visualizations and confusion matrices.

---

## 🚀 Workflow
1. **Pre-processing:** Checking for null values and duplicates (the dataset has 1025 records).
2. **Feature Engineering:** Scaling numerical features to ensure the Logistic Regression model performs optimally.
3. **Model Implementation:** Training the `LogisticRegression` classifier from Scikit-Learn.
4. **Validation:** Using a Confusion Matrix and Classification Report to verify model sensitivity and specificity.



---

## 📉 Results & Insights
- Features like **Chest Pain (CP)** and **Maximum Heart Rate (Thalach)** show a strong positive correlation with heart disease.
- **Logistic Regression** proves to be an efficient baseline for this medical classification task due to its interpretability.

---

## 📝 Installation & Usage
1. Clone this repository.
2. Install the required packages: `pip install pandas scikit-learn seaborn`.
3. Open the Jupyter Notebook or run the Python script to see the prediction results.

---
