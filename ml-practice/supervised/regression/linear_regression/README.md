# 🎓 Student Performance Prediction using Linear Regression

## 📌 Project Overview
This project aims to predict the **Performance Index** of students based on several academic and lifestyle factors. By leveraging **Linear Regression**, we analyze how study habits, previous academic records, and daily routines impact a student's final performance score.

---

## 🧩 Problem Statement
The goal is to build a predictive model that estimates a student's performance (on a scale of 10 to 100). This helps educators and students identify which factors contribute most significantly to academic success.

---

## 📊 Dataset Information

### 🏷️ Dataset Name  
Student Performance Dataset

### 🌐 Source  
Kaggle / Student_Performance.csv

### 📐 Dataset Shape
- **Total Rows:** 10,000  
- **Total Columns:** 6  

---

## 🧬 Dataset Columns & Descriptions

| Column Name | Description |
| :--- | :--- |
| **Hours Studied** | Total number of hours spent studying. |
| **Previous Scores** | Scores obtained by the student in previous exams. |
| **Sleep Hours** | Average number of hours the student sleeps per day. |
| **Sample Question Papers** | Number of practice papers the student has solved. |
| **Performance Index** | **(Target)** The final performance score (10.0 - 100.0). |

---

## 🎯 Features and Target Variable

### 🔹 Features (X)
To train our model, we use the following independent variables:
1. `Hours Studied`
2. `Previous Scores`
3. `Sleep Hours`
4. `Sample Question Papers Practiced`

### 🎯 Target (y)
- `Performance Index`: The continuous numerical value we aim to predict.

---

## 🛠️ Tech Stack Used
- **Language:** Python 3.x
- **Libraries:** - `Pandas` (Data Manipulation)
  - `NumPy` (Numerical Computation)
  - `Scikit-Learn` (Machine Learning Model & Scaling)
  - `Matplotlib` / `Seaborn` (Data Visualization)

---

## 📚 Project Workflow

1.  **Data Loading:** Importing the dataset from CSV.
2.  **Exploratory Data Analysis (EDA):** Visualizing correlations between study hours and performance.
3.  **Data Preprocessing:**- Checking for missing values.
4.  **Data Splitting:** Dividing the data into **80% Training** and **20% Testing** sets.
5.  **Model Building:** Implementing the **Linear Regression** algorithm.
6.  **Model Evaluation:** Checking accuracy using
---

## 📈 Key Insights
- **Hours Studied** and **Previous Scores** typically show the strongest positive correlation with the Performance Index.
- Regular practice with **Sample Question Papers** provides a measurable boost to student confidence and results.

---

## 🚀 How to Run
1. Clone this repository.
2. Install dependencies: `pip install pandas scikit-learn matplotlib seaborn`.
3. Run the Jupyter Notebook or Python script.

---