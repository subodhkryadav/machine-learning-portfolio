# 🚗 Used Car Price Prediction using AdaBoost Regressor

## 📌 Project Summary
This project implements a machine learning solution to estimate the resale value of used cars. By utilizing the **AdaBoost (Adaptive Boosting)** algorithm, the model learns from a series of weak learners (Decision Trees) to build a powerful predictor that accounts for both technical specifications and market conditions.

---

## 🧩 Why AdaBoost?
Pricing data for cars often contains outliers and non-linear relationships. **AdaBoost** is particularly effective here because it focuses more on previous prediction errors, iteratively improving the model's accuracy. This ensures that even complex factors like the "Age vs. Mileage" trade-off are captured effectively.

---

## 📊 Dataset Overview
The data represents over 15,000 car listings from CarDekho, including key details like engine power, fuel type, and ownership history.



### 📐 Key Metrics
- **Observations:** 15,411
- **Features:** 12 Independent variables
- **Algorithm:** AdaBoost Regressor

---

## 🧬 Feature Breakdown

| Feature | Importance |
| :--- | :--- |
| **Max Power** | Highly correlated with higher pricing in luxury and sports segments. |
| **Vehicle Age** | The most significant factor for depreciation. |
| **Transmission** | Automatic vehicles generally carry a premium in the used market. |
| **KM Driven** | Reflects the wear and tear of the vehicle. |

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries**:
  - `Scikit-Learn`: For AdaBoost, Preprocessing, and Metrics.
  - `Pandas & NumPy`: For efficient data manipulation.
  - `Matplotlib & Seaborn`: For statistical plotting.

---

## 🚀 Execution Workflow
1. **Cleaning**: Removing unnecessary data and handling null values.
2. **Transformation**: Applying `ColumnTransformer` to handle both numerical and categorical data simultaneously.
3. **Training**: Fitting the `AdaBoostRegressor` on the training subset.
4. **Performance Check**: Evaluating the model using the $R^2$ score to determine how much of the price variance is explained by our features.

---

## 📈 Conclusion
The **AdaBoost** model provides a reliable price suggestion engine. This can be integrated into web applications to give new sellers an instant valuation based on current market conditions in India.

---

## 📝 Usage
1. Open the `Adaboost_regression.ipynb` notebook.
2. Ensure the CarDekho dataset is present in the working directory.
3. Run the cells to process the data, train the model, and see the final accuracy scores.