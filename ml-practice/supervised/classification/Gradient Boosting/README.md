# ✈️ Holiday Package Prediction using Gradient Boosting Classifier

## 📌 Project Summary
This project aims to optimize the marketing strategy for "Tips & Travel.com" by predicting customer purchase behavior for a new travel package. We utilize a **Gradient Boosting Classifier**, a powerful ensemble learning technique, to identify the most likely buyers based on their social and economic profiles.

---

## 🧩 The Business Problem
Marketing costs are significantly higher when leads are contacted at random. To minimize expenditure and maximize conversion for the new **Wellness Tourism Package**, this project builds a classification model that predicts lead conversion with high sensitivity and specificity.

---

## 📊 Dataset Overview
The dataset includes approximately 4,900 customer profiles with information ranging from monthly income and hotel preferences to specific behaviors like response to sales pitches and follow-up history.



---

## 🧬 Feature Analysis

| Feature | Importance |
| :--- | :--- |
| **Passport** | Possession of a passport is one of the highest indicators of travel probability. |
| **MonthlyIncome** | Directly affects the ability to purchase luxury or wellness packages. |
| **Designation** | Reflects the professional status and available disposable income. |
| **Age** | Helps in segmenting the audience for specific wellness activities. |

---

## 🛠️ Tech Stack
- **Python**: Main programming language.
- **Libraries**:
  - `Scikit-Learn`: For the Gradient Boosting model, Scaling, and Evaluation.
  - `Pandas & NumPy`: For data cleaning and feature transformation.
  - `Plotly & Seaborn`: For interactive and static data visualization.
  - `Joblib`: For model persistence and serialization.

---

## 🚀 Execution Workflow
1. **Data Imputation**: Filling missing values in critical columns like `Age` and `MonthlyIncome`.
2. **Encoding & Scaling**: Normalizing features to ensure the boosting algorithm converges efficiently.
3. **Algorithm Implementation**: Utilizing `GradientBoostingClassifier` to iteratively correct errors from previous decision trees.
4. **Validation**: Using **Precision** and **Recall** as primary metrics to ensure the marketing team focuses on high-quality leads.

---

## 📈 Conclusion
The **Gradient Boosting** approach outperforms simple classifiers by handling non-linear relationships and interactions between features like `MonthlyIncome` and `NumberOfTrips` effectively.

---

## 📝 Usage
1. Open the `Gradient_Boosting_Classifier.ipynb` notebook.
2. Ensure the `Travel.csv` file is available in the root folder.
3. Run all cells to generate the model and view the classification reports.