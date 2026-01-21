# 🍷 Wine Quality Prediction using Support Vector Machine (SVC)

## 📌 Project Summary
This project focuses on the classification of wine quality using the **Support Vector Classifier (SVC)**. The goal is to leverage chemical analysis data to predict the sensory quality of wine, providing a digital tool for quality control in the beverage industry.

---

## 🧩 Methodology: Support Vector Classifier
We chose **SVC** for this task because of its effectiveness in high-dimensional spaces. By using the "Kernel Trick," the model can create non-linear decision boundaries to separate different wine quality classes effectively.



---

## 📊 Dataset Overview
The dataset contains various chemical attributes of wines. These attributes are the result of complex biochemical processes during wine production.

### 📐 Key Metrics
- **Algorithm:** SVC (Support Vector Classifier)
- **Primary Features:** Alcohol, pH, Sulphates, and Volatile Acidity.
- **Task:** Multi-class Classification.

---

## 🧬 Feature Analysis

| Feature | Impact on Quality |
| :--- | :--- |
| **Alcohol** | Usually has a positive correlation with higher quality ratings. |
| **Volatile Acidity** | High levels can lead to an unpleasant, vinegar-like taste, reducing quality. |
| **Sulphates** | Act as an antimicrobial and antioxidant, affecting the wine's longevity and grade. |

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries**:
  - `Scikit-Learn`: For the SVC model and evaluation.
  - `Pandas & NumPy`: For data handling.
  - `Matplotlib & Seaborn`: For visualization.
  - `YData-Profiling`: For comprehensive data reports.

---

## 🚀 Execution Workflow
1. **Profiling**: Running `ProfileReport` to get deep insights into the wine chemistry.
2. **Setup**: Preparing `x` (features) and `y` (quality) for the model.
3. **SVC Implementation**: Training the model with specific kernels (e.g., `linear`).
4. **Validation**: Testing the model on unseen data to check the accuracy.

---

## 📈 Conclusion
The **Support Vector Classifier** provides a robust framework for wine classification. With proper scaling and kernel tuning, the model can accurately categorize wines, aiding producers in maintaining consistent quality standards.

---

## 📝 Usage
1. Load `wine_dataset_svc.ipynb` in a Jupyter environment.
2. Ensure you have the dataset file in the same directory.
3. Execute the cells to see the profiling report and model accuracy.