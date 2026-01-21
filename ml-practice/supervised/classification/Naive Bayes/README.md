# 🤖 Probabilistic Machine Learning: Naive Bayes Classification Suite

## 📌 Project Summary
This repository contains two comprehensive machine learning projects using the **Naive Bayes** algorithm. These projects demonstrate how probabilistic models can be applied to both medical diagnostics (Diabetes) and socio-economic classification (Income Level).



---

## 📂 Included Projects
1. **Diabetes Prediction**: Predicting health outcomes based on medical metrics.
2. **Income Level Classification**: Predicting whether a person's income exceeds $50K/year using census data.

---

## 🧩 Why Naive Bayes?
Naive Bayes is a powerful algorithm based on Bayes' Theorem. In these projects, it was chosen for:
- **Efficiency**: Extremely fast training and prediction times.
- **Performance**: Working well with high-dimensional data (like the Adult dataset).
- **Simplicity**: Providing a strong baseline model for classification tasks.

---

## 📊 Technical Comparison

| Feature | Diabetes Project | Income Project |
| :--- | :--- | :--- |
| **Problem Type** | Binary Classification (Medical) | Binary Classification (Census) |
| **Model** | GaussianNB | GaussianNB |
| **Main Challenge** | Feature Scaling | Categorical Data & Missing Values |
| **Evaluation** | Accuracy Score | ROC-AUC & Cross-Validation |

---

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**:
  - `Scikit-Learn`: Model training, metrics, and cross-validation.
  - `Pandas & NumPy`: Data cleaning and engineering.
  - `Matplotlib & Seaborn`: Visualization of results.

---

## 📈 Key Insights
- In the **Diabetes** project, glucose levels and BMI emerged as the most significant features.
- In the **Income** project, we achieved an accuracy of ~80%, significantly outperforming the null accuracy of ~75%, proving that the model captures meaningful patterns in socio-economic data.

---

## 🚀 How to Execute
1. Clone the repository.
2. Install requirements: `pip install pandas scikit-learn seaborn`.
3. Run `Diabetes Prediction.ipynb` for medical analysis.
4. Run `Naive Bayes Classification.ipynb` for census data analysis.

---

## 📝 Conclusion
These projects highlight the robustness of the Naive Bayes algorithm in different domains. While simple, the algorithm provides high reliability when data is properly scaled and categorical features are engineered correctly.