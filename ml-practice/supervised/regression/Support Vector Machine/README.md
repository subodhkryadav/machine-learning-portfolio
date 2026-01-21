# 🎓 Graduate Admission Prediction using SVR

## 📌 Project Summary
This project implements a machine learning solution to estimate the probability of graduate school admission. By utilizing the **Support Vector Regression (SVR)** algorithm, the model identifies complex patterns in academic profiles, providing a reliable estimate of a student's chances based on historical data.

---

## 🧩 Why SVR?
Predicting admissions involves non-linear relationships where traditional linear models might fail. **SVR** is effective here because it uses kernels to handle high-dimensional data and focuses on maintaining errors within a specified threshold (epsilon-tube), making it robust to outliers.

---

## 📊 Dataset Overview
The data represents student profiles including GRE, TOEFL, and CGPA, which are critical metrics used by universities worldwide for the admission process.

### 📐 Key Metrics
- **Observations:** 500
- **Features:** 7 Independent variables
- **Algorithm:** Support Vector Regressor (SVR)

---

## 🧬 Feature Breakdown

| Feature | Importance |
| :--- | :--- |
| **CGPA** | The most significant indicator of long-term academic consistency. |
| **GRE Score** | Reflected as a primary filter for technical and analytical readiness. |
| **Research** | Adds a significant boost to the probability for top-tier universities. |
| **SOP/LOR** | Qualitative measures converted into quantitative strengths. |

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries**:
  - `Scikit-Learn`: For SVR, Preprocessing, and GridSearchCV.
  - `Pandas & NumPy`: For data manipulation.
  - `Matplotlib & Seaborn`: For statistical plotting and heatmaps.

---

## 🚀 Execution Workflow
1. **Cleaning**: Dropping `Serial No.` and checking for null values.
2. **Scaling**: Applying `StandardScaler` so that high-range values (GRE) don't overpower low-range values (CGPA).
3. **Training**: Fitting the `SVR` model using optimized hyperparameters.
4. **Performance Check**: Using **Learning Curves** to visualize how the model improves with more data and ensuring it generalizes well.

---

## 📈 Conclusion
The **SVR** model provides a high-precision tool for admission prediction. This can be used by educational consultants to guide students in choosing universities that match their academic standing.

---

## 📝 Usage
1. Open the `svr.ipynb` notebook.
2. Ensure the `Admission_Predict.csv` dataset is in the working directory.
3. Run the cells to process the data, train the model, and see the final $R^2$ scores.