# ✈️ Holiday Package Prediction using Random Forest

## 📌 Project Description
This project is built for a travel company to optimize its marketing expenditure. By analyzing customer data, we use a **Random Forest Classifier** to predict which customers are likely to purchase a newly introduced **Wellness Tourism Package**. This data-driven approach helps target the right audience instead of contacting customers at random.

---

## 🧩 The Challenge
Marketing costs are high when target audiences are chosen randomly. With only an 18% conversion rate in the previous year, the goal is to use Machine Learning to increase the efficiency of the marketing team by providing them with a "likelihood to buy" score for each lead.

---

## 📊 Dataset Summary
The dataset contains information about existing and potential customers, covering their financial status, travel preferences, and previous interactions with the company.



---

## 🧬 Key Features

| Feature | Description |
| :--- | :--- |
| **Passport** | Having a passport is a strong indicator of travel intent. |
| **MonthlyIncome** | Financial capacity to afford premium packages. |
| **DurationOfPitch**| More time spent in pitching often leads to higher conversions. |
| **Designation** | Professional level of the customer. |
| **ProdTaken** | **(Target)** 1 if the customer bought the package, 0 otherwise. |

---

## 🛠️ Tech Stack
- **Python**: Primary language.
- **Libraries**:
  - `Scikit-Learn`: For the Random Forest ensemble model.
  - `Pandas`: For extensive data preprocessing.
  - `Matplotlib/Seaborn`: For generating ROC-AUC curves and Feature Importance plots.

---

## 🚀 Workflow in Notebook
1. **EDA & Visualization**: Analyzing how income and age affect purchasing decisions.
2. **Data Transformation**: Label encoding for categorical variables.
3. **Model Selection**: Using **Random Forest** due to its ability to handle complex non-linear relationships and prevent overfitting.
4. **Evaluation**: Using the **ROC (Receiver Operating Characteristic)** curve to measure the model's sensitivity and specificity.



---

## 📈 Conclusion
The model highlights that **Passport** ownership, **Monthly Income**, and **Age** are the top predictors for purchasing a travel package. Implementing this model can significantly reduce the cost per acquisition for the company.

---

## 📝 Usage
1. Open the `Random_Forest_Classifier.ipynb` notebook.
2. Ensure the dataset is in the same directory.
3. Run all cells to see the training process and evaluation metrics.

---