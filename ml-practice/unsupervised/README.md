# 📂 Unsupervised Machine Learning: Portfolio

## 📌 Project Overview
This repository contains a collection of **Unsupervised Learning** implementations. The projects focus on finding hidden patterns, grouping data points, and reducing dimensionality without the need for labeled outcomes. It covers Clustering and Dimensionality Reduction techniques using industry-standard datasets.

---

## 🛠️ Algorithms & Techniques Implemented

### 1. K-Means Clustering
- **Project:** Customer Segmentation using Mall Data.
- **Key Concepts:** WCSS, Elbow Method for finding optimal $K$, and Centroid initialization.
- **Objective:** Grouping customers based on income and spending habits.


### 2. DBSCAN (Density-Based Clustering)
- **Project:** Identifying high-density customer segments.
- **Key Concepts:** Epsilon ($\epsilon$), Min Samples, and Noise/Outlier detection.
- **Objective:** Finding clusters of arbitrary shapes and handling spatial noise effectively.


### 3. Hierarchical Clustering
- **Project:** Species segmentation using the Iris Dataset.
- **Key Concepts:** Dendrograms, Agglomerative approach, and Ward's Linkage.
- **Objective:** Building a tree-like hierarchy to understand biological data relationships.


### 4. Principal Component Analysis (PCA)
- **Project:** Dimension reduction on Glass Classification data.
- **Key Concepts:** Covariance Matrix, Eigenvectors, and Explained Variance Ratio (EVR).
- **Objective:** Reducing feature noise and simplifying high-dimensional datasets for better model performance.


---

## 📊 Evaluation Metrics Used
- **Silhouette Score:** To measure how well-separated the clusters are.
- **WCSS (Within-Cluster Sum of Squares):** To evaluate K-Means compactness.
- **Dendrogram Analysis:** To visually determine the number of hierarchical groups.
- **Cumulative Explained Variance:** To select the optimal number of principal components.

---

## ⚙️ Tech Stack
- **Languages:** Python
- **Libraries:** Scikit-Learn, SciPy (for Dendrograms), Pandas, NumPy.
- **Visualization:** Matplotlib, Seaborn.
- **EDA:** YData-Profiling for automated data insights.

---

## 🚀 Navigation
Each algorithm is implemented in its own dedicated Jupyter Notebook. You can find detailed Exploratory Data Analysis (EDA) and step-by-step model implementation in the respective files:
- `KMeans.ipynb`
- `DBSCAN.ipynb`
- `Hierarchical_clustering.ipynb`
- `PCA.ipynb`