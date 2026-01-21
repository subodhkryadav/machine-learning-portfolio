# 📈 Gold Price Prediction using Random Forest Regressor

## 📌 Project Overview
Gold has always been a significant investment asset. Predicting its price accurately is a complex task due to its dependence on various global economic factors. This project implements a **Machine Learning Regression Model** to predict the price of the **SPDR Gold Shares ETF (GLD)** based on key financial indicators.

---

## 🧩 Problem Statement
The goal of this project is to build a high-accuracy regression model that estimates gold prices. By analyzing the relationship between the S&P 500 index, Silver prices, Oil prices, and currency exchange rates (EUR/USD), we aim to provide a reliable forecasting tool for investors and financial analysts.

---

## 📊 Dataset Information

### 🏷️ Dataset Name  
Gold Price Data (GLD)

### 🌐 Source  
Historical Financial Market Data

### 📐 Dataset Shape
- **Total Rows:** 2,290  
- **Total Columns:** 6  

---

## 🧬 Dataset Features (Input Variables)

| Feature | Description |
| :--- | :--- |
| **SPX** | The Standard & Poor's 500 stock market index. |
| **USO** | United States Oil Fund price (Oil prices). |
| **SLV** | iShares Silver Trust price (Silver prices). |
| **EUR/USD** | The exchange rate between the Euro and the US Dollar. |

### 🎯 Target Variable
- **GLD**: The price of the SPDR Gold Shares ETF.

---

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Libraries**:
  - `Pandas`: Data manipulation and cleaning.
  - `NumPy`: Numerical operations.
  - `Scikit-Learn`: Model training (Random Forest) and evaluation.
  - `Seaborn & Matplotlib`: For correlation heatmaps and trend visualization.

---

## 📚 Project Workflow

1. **Data Loading**: Importing the `gld_price_data.csv`.
2. **Exploratory Data Analysis (EDA)**: Checking for null values and statistical summaries.
3. **Correlation Analysis**: Using a Heatmap to understand how Silver and the S&P 500 correlate with Gold prices.

4. **Data Splitting**: Separating the data into Training (80%) and Testing (20%) sets.
5. **Model Building**: Training the **Random Forest Regressor** (an ensemble learning method).
6. **Model Evaluation**: Measuring performance using:
   - **R-squared ($R^2$) Score**
   - **Mean Absolute Error (MAE)**
7. **Visualization**: Plotting Actual vs. Predicted gold prices to check for accuracy.


---

## 📈 Key Insights
- **Silver Prices (SLV)**: Usually show a very high positive correlation with Gold prices.
- **Ensemble Learning**: Random Forest is highly effective for this dataset as it handles the non-linear relationships between various market indices better than simple Linear Regression.

---

## 🚀 How to Run
1. Clone the repository.
2. Install the necessary libraries: `pip install pandas scikit-learn seaborn matplotlib`.
3. Run the Python script or Jupyter Notebook.

---