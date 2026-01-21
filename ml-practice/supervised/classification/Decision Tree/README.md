# 🩺 Pima Indians Diabetes Prediction using Decision Tree Classifier

## 📌 Project Overview
This project aims to predict the onset of diabetes in female patients from the Pima Indian community. By utilizing the **Decision Tree Classifier**, we analyze medical diagnostic measurements to build a model that can accurately distinguish between diabetic and non-diabetic individuals.

---

## 🧩 Problem Statement
The goal is to develop a predictive diagnostic tool. Given several health-related variables such as Glucose levels, BMI, and Age, the model must classify whether a patient has diabetes (Target: 1) or not (Target: 0).

---

## 📊 Dataset Information

### 🏷️ Dataset Name  
Pima Indians Diabetes Dataset

### 🌐 Source  
UCI Machine Learning Repository

### 📐 Dataset Shape
- **Total Rows:** 768  
- **Total Columns:** 9  

---

## 🧬 Dataset Columns & Descriptions

| Column | Description |
| :--- | :--- |
| **Pregnancies** | Number of times pregnant. |
| **Glucose** | Plasma glucose concentration (a 2-hour oral glucose tolerance test). |
| **BloodPressure** | Diastolic blood pressure (mm Hg). |
| **SkinThickness** | Triceps skinfold thickness (mm). |
| **Insulin** | 2-Hour serum insulin (mu U/ml). |
| **BMI** | Body mass index (weight in kg/(height in m)^2). |
| **PedigreeFunction** | Diabetes pedigree function (genetic score). |
| **Age** | Age in years. |
| **Outcome** | **Target Variable** (0: Non-Diabetic, 1: Diabetic). |

---

## 🎯 Features and Target Variables

### 🔹 Features (X)
The model utilizes 8 clinical features:
*Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age.*

### 🎯 Target (y)
* **Outcome**: Binary classification (0 or 1).

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Libraries**:
  - `Pandas`: For data manipulation and loading.
  - `Scikit-Learn`: For model building, hyperparameter tuning, and evaluation.
  - `Matplotlib/Seaborn`: For data exploration and tree visualization.

---

## 📚 Project Workflow

1.  **Data Loading**: Importing the dataset directly from the source URL.
2.  **Exploratory Data Analysis (EDA)**: Understanding data distribution and identifying patterns.
3.  **Feature Selection**: Assigning independent variables (X) and the target variable (y).
4.  **Model Training**: Implementing the `DecisionTreeClassifier`.
5.  **Hyperparameter Tuning**: Finding the best parameters (like `max_depth` or `criterion`) to optimize accuracy and prevent overfitting.
6.  **Visualization**: Generating a visual map of the Decision Tree to understand the decision-making logic.

7.  **Performance Evaluation**: Measuring the model using accuracy scores and confusion matrices.
8.  **Interpretation**: Analyzing which medical factors (like Glucose or BMI) are the most significant predictors of diabetes.

---

## 🚀 How to Use
1. Clone this repository.
2. Install dependencies: `pip install pandas scikit-learn matplotlib seaborn`.
3. Run the notebook or script to train the model and view the prediction results.

---