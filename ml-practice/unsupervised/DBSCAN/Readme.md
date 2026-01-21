# 📍 Unsupervised Learning: DBSCAN Clustering Portfolio

## 📌 Project Overview
This project implements the **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) algorithm to segment mall customers. This density-based approach is superior to K-Means for datasets with irregular shapes and for identifying outliers in customer behavior.

---

## 🛠️ Algorithm Implemented: DBSCAN
- **Core Concept**: Groups together points that are closely packed together (points with many nearby neighbors).
- **Outlier Detection**: Automatically marks points in low-density regions as **Noise (-1)**.
- **No K-Requirement**: Unlike K-Means, DBSCAN does not require the number of clusters to be specified in advance.

---

## 📊 Technical Workflow
1. **Data Preprocessing**: Loading the `Mall_Customers.csv` and selecting key features.
2. **Epsilon ($\epsilon$) Selection**: Defining the maximum distance between two samples for them to be considered as in the same neighborhood.
3. **Min Samples**: Defining the number of samples in a neighborhood for a point to be considered as a core point.
4. **Visualization**: Plotting clusters using Income vs. Spending Score.
5. **Metric**: Using the **Silhouette Score** to measure how similar an object is to its own cluster compared to other clusters.

---

## ⚙️ Tech Stack
- **Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Scikit-Learn.

---

## 📉 Performance Evaluation
- **Clusters Found**: Identified distinct segments of customers based on density.
- **Silhouette Score**: Validated the separation and cohesion of the formed clusters.