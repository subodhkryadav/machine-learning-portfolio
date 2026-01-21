# 🚗 Car Selling Price Prediction using Gradient Boosting

## 📌 Project Summary
This project is designed to estimate the market value of used cars using machine learning. By implementing a **Gradient Boosting Regressor**, we can predict the `selling_price` with high precision by considering multiple factors like usage, engine specifications, and brand value.

---

## 🧩 The Business Problem
Valuing a used car is challenging because it depends on many non-linear factors (e.g., a car's price drops significantly as it gets older, but high engine power can keep the value up). Standard linear models often fail here. **Gradient Boosting** is used because it builds trees sequentially to minimize errors, making it perfect for complex pricing data.

---

## 📊 Dataset Insights
The dataset contains cleaned and imputed data of used cars, featuring both technical specs and market-related information.

### 📐 Key Metrics
- **Observations:** Large-scale vehicle records.
- **Input Features:** 10 Independent variables.
- **Algorithm:** Gradient Boosting (Ensemble Learning).

---

## 🧬 Feature Analysis

| Feature | Impact on Price |
| :--- | :--- |
| **Vehicle Age** | Strong negative impact (Older cars = Lower price). |
| **Transmission** | Automatic cars usually command a higher price. |
| **Max Power** | Higher horsepower strongly increases the valuation. |
| **KM Driven** | High mileage generally reduces the resale value. |

---

## 🛠️ Tech Stack
- **Python**: Core programming.
- **Libraries**:
  - `Scikit-Learn`: For Gradient Boosting implementation.
  - `Pandas & NumPy`: For data manipulation and encoding.
  - `Seaborn & Plotly`: For creating interactive visualizations and correlation heatmaps.

---

## 🚀 Execution Workflow
1. **Preprocessing**: Dropping IDs and brand names to focus on the model and technical specs.
2. **Label Encoding**: Transforming text categories into numbers that the model can understand.
3. **Training**: Fitting the `GradientBoostingRegressor` to the training data.
4. **Evaluation**: Calculating **R² Score** and **RMSE** for both training and testing sets to ensure the model generalizes well without overfitting.

---

## 📉 Conclusion
The **Gradient Boosting** model effectively captures the depreciation patterns and performance-based value of vehicles, making it a robust tool for car dealerships and online marketplaces.

---

## 📝 Usage
1. Open the `Gradient Boosting Regressior.ipynb` file.
2. Place the `cardekho_imputated.csv` in the same directory.
3. Run all cells to see the metrics and price predictions.