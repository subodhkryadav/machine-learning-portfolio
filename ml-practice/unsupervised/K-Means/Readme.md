# 📍 Unsupervised Learning: K-Means Clustering Suite

## 📌 Overview
This repository contains implementations of the **K-Means Clustering** algorithm applied to retail data. The goal is to perform **Customer Segmentation**, allowing businesses to identify high-value customers and optimize marketing efforts.

---

## 🛠️ Algorithm: K-Means Clustering
K-Means is a centroid-based clustering algorithm that partitions data into $K$ non-overlapping subgroups.
- **Distance Metric**: Euclidean Distance.
- **Optimization**: Elbow Method (WCSS) to determine the best number of clusters.

---

## 📂 Project Structure
1. **KMeans_0.ipynb**: Initial implementation focusing on data profiling and basic cluster visualization.
2. **KMeans.ipynb**: Enhanced analysis with advanced plotting (Seaborn) and centroid identification.

---

## 📊 Evaluation & Metrics
- **WCSS (Within-Cluster Sum of Squares)**: Used to measure the compactness of clusters.
- **Elbow Point**: Selected based on the significant drop in WCSS.
- **Centroids**: Identified the representative point for each customer segment.

---

## ⚙️ Tech Stack
- **Language**: Python
- **Libraries**: Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn.
- **EDA Tool**: YData-Profiling.

---

## 🚀 Key Insights
- Identified 5 distinct customer segments (e.g., High Income/Low Spending, High Income/High Spending, etc.).
- Successfully mapped the "Target" group for personalized marketing campaigns.