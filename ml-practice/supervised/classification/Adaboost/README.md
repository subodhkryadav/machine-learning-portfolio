# ✈️ Holiday Package Prediction using AdaBoost Classifier

## 📌 Project Summary
This project focuses on predicting customer behavior for a travel company's new product offering. By using the **AdaBoost Classifier**, an ensemble learning method, we create a strong predictive model from multiple weak learners (Decision Trees) to accurately identify potential buyers of a wellness tourism package.

---

## 🧩 The Business Case
In the previous year, only 18% of customers purchased packages because marketing efforts were directed randomly. This project utilizes machine learning to prioritize leads, thereby reducing the cost of customer acquisition and increasing the overall conversion rate for "Tips & Travel.com".

---

## 📊 Dataset Overview
The data consists of 4,888 customer profiles. It includes features like marital status, passport ownership, and previous trip history, which are critical in determining travel intent.



### 📐 Key Metrics
- **Observations:** 4,888
- **Algorithm:** AdaBoost Classifier
- **Primary Goal:** High Recall for potential buyers

---

## 🧬 Key Features

| Feature | Importance |
| :--- | :--- |
| **Passport** | Customers with passports are significantly more likely to purchase international packages. |
| **Monthly Income** | A key indicator of the customer's purchasing power for premium packages. |
| **Total Visiting** | Combined family size (Adults + Children) influences the choice of package type. |
| **Pitch Duration** | Longer engagement during pitches often correlates with higher interest levels. |

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries**:
  - `Scikit-Learn`: For the AdaBoost model, ColumnTransformer, and Pipeline.
  - `Pandas & NumPy`: For data cleaning and feature engineering.
  - `Seaborn & Plotly`: For interactive data visualization.

---

## 🚀 Project Workflow
1. **Handling Missing Data**: Strategic imputation of missing values in age and income.
2. **Pipeline Creation**: Implementing a clean preprocessing pipeline using `OneHotEncoder` and `StandardScaler`.
3. **Model Selection**: Comparing **AdaBoost** against other ensemble methods like Random Forest to find the best fit.
4. **Final Evaluation**: Generating the **ROC-AUC Curve** to visualize the trade-off between sensitivity and specificity.

---

## 📈 Conclusion
The **AdaBoost Classifier** proves to be effective in handling the imbalance and non-linearity in travel marketing data, allowing for more precise targeting of wellness tourism packages.

---

## 📝 How to Run
1. Ensure `Travel.csv` is in the same folder as the notebook.
2. Open `Adaboost Classification.ipynb` in Jupyter or VS Code.
3. Run all cells to see the comparative analysis and final model evaluation.