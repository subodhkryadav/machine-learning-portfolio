# 🍷 Wine Classification using K-Nearest Neighbors (KNN)

## 📌 Project Summary
This repository contains a machine learning solution to classify wine quality based on chemical constituents. The project primarily focuses on the **K-Nearest Neighbors (KNN)** algorithm, optimized through cross-validation to ensure high classification accuracy.

---

## 🧩 Why KNN?
KNN is a non-parametric, lazy learning algorithm that classifies data points based on the similarity of their neighbors. In wine classification, chemical profiles of high-quality wines tend to cluster together, making KNN an ideal choice for identifying patterns without assuming a specific underlying data distribution.



---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries**:
  - `Scikit-Learn`: For KNN, GridSearchCV, and model evaluation.
  - `Pandas & NumPy`: For data cleaning and matrix operations.
  - `YData-Profiling`: For automated Exploratory Data Analysis (EDA).
  - `Joblib`: For exporting the final trained model.

---

## 🧬 Feature Engineering & Analysis
Before training, the dataset was analyzed for correlations between alcohol content, pH, and sulphates. A **Grid Search** was implemented to fine-tune the $k$ parameter, ensuring the model is neither overfitted nor underfitted.

---

## 📊 Model Evaluation Results
The model's performance is evaluated using a Confusion Matrix to track True Positives and True Negatives across different wine classes.



### Key Metrics:
- **Accuracy**: Overall correctness of the model.
- **Precision & Recall**: Critical for understanding how well the model identifies specific quality grades.
- **F1-Score**: The harmonic mean of precision and recall.

---

## 🚀 Execution Workflow
1. **Load Data**: Import the `wine_dataset`.
2. **EDA**: Generate a `ProfileReport` to understand feature importance.
3. **Train/Test Split**: Divide data (e.g., 80/20) for validation.
4. **Grid Search**: Execute `GridSearchCV` to find the best $k$ for `KNeighborsClassifier`.
5. **Save Model**: Export the result to `knn_model.pkl` for deployment.

---

## 📝 How to Use
1. Clone the repo and ensure all dependencies are installed.
2. Run the `K-Nearest Neighbors classification.ipynb` notebook.
3. Use `joblib.load('knn_model.pkl')` to use the trained model on new wine data samples.