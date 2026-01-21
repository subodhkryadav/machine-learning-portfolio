# 🎓 College Placement Prediction using Logistic Regression

## 📌 Project Description
This repository contains a Machine Learning project designed to predict **Student Placement** outcomes. Using **Logistic Regression**, the model classifies students into "Placed" or "Not Placed" categories by analyzing various performance metrics such as CGPA, IQ, and Internship experience.

---

## 🧩 The Challenge
In the final year of college, students are often anxious about their career prospects. This project provides a data-driven approach to help students understand which areas (like projects or communication skills) they need to improve to increase their chances of being hired.

---

## 📊 Dataset Summary
The dataset consists of 500 student records with a mix of numerical and categorical data.



### 📐 Key Statistics
- **Total Observations:** 500
- **Independent Variables:** 9
- **Dependent Variable:** Placement (Yes/No)

---

## 🧬 Feature breakdown

| Feature | Type | Description |
| :--- | :--- | :--- |
| **IQ** | Numerical | Mental aptitude score |
| **CGPA** | Numerical | Academic grade point average |
| **Internship** | Categorical | Industrial exposure (Yes/No) |
| **Projects** | Numerical | Count of completed technical projects |
| **Communication**| Numerical | Proficiency rating |
| **Placement** | **Target** | Placement Status (1: Yes, 0: No) |

---

## 🛠️ Technology Stack
- **Python 3.x**
- **Libraries:**
  - `Pandas`: For data manipulation.
  - `Scikit-Learn`: For the Logistic Regression algorithm and metrics.
  - `Matplotlib/Seaborn`: For generating correlation heatmaps and plots.

---

## 🚀 Project Workflow
1. **Data Preprocessing:** Handle categorical strings and scale numerical features if necessary.
2. **Exploratory Data Analysis (EDA):** Visualize how CGPA and IQ impact placement trends.
3. **Model Selection:** Utilizing **Logistic Regression** due to the binary nature of the target variable.
4. **Performance Metrics:** - Accuracy Score
   - Precision and Recall
   - Confusion Matrix
5. **Results:** Identifying the most influential factors for a successful placement.

---

## 📈 Conclusion
The model demonstrates that factors like **CGPA** and **Internship Experience** are the strongest indicators of whether a student will be successfully placed during campus recruitment.

---

## 📝 Usage
1. Clone the repository.
2. Ensure `CollegePlacement.csv` is in the root directory.
3. Run the analysis script or Jupyter Notebook.

---