 # 🏠 House Rent Prediction using KNN & Ensemble Regressors

## 📌 Project Summary
This machine learning project predicts house rents in major Indian cities. It implements a multi-model approach, evaluating the performance of **KNN**, **Random Forest**, and **AdaBoost** to determine which algorithm best captures the pricing dynamics of the rental market.

---

## 🧩 Methodology
The project follows a standard data science pipeline:
- **Preprocessing**: Rigorous outlier detection was performed on `Size` and `Bathroom` counts to ensure model stability.
- **Encoding**: Categorical data was converted using One-Hot Encoding to make it compatible with distance-based (KNN) and tree-based models.
- **Optimization**: Hyperparameter tuning was conducted via `GridSearchCV` to optimize $k$ in KNN and $n\_estimators$ in ensemble models.

---

## 📊 Feature Analysis

| Feature | Impact |
| :--- | :--- |
| **Size** | High correlation; as sq. ft. increases, rent usually scales exponentially in metro cities. |
| **City** | Locations like Mumbai show a significantly higher baseline rent compared to others. |
| **Furnishing** | Furnished apartments command a premium over unfurnished ones. |
| **BHK** | Influences the price but is highly dependent on the total house size. |

---

## 🛠️ Tech Stack
- **Python**: Core programming.
- **Libraries**:
  - `Scikit-Learn`: KNN, Random Forest, AdaBoost, GridSearchCV.
  - `Pandas & NumPy`: Data manipulation.
  - `Matplotlib & Seaborn`: Visualization and distribution analysis.

---

## 📈 Model Evaluation
The models were evaluated using **Mean Squared Error (MSE)**. 
- **KNN**: Good for local patterns but sensitive to outliers.
- **Random Forest**: Strong performer that handled the non-linear relationship between size and city well.
- **AdaBoost**: Iteratively improved the prediction accuracy by focusing on high-error instances.

---

## 🚀 How to Use
1. Clone the repository.
2. Place the `House_Rent_Dataset.csv` in the project directory.
3. Run the `house-rental-prediction.ipynb` notebook to see the data processing and model comparison results.