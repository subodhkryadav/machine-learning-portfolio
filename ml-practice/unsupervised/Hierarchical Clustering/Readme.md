# 🌳 Unsupervised Learning: Hierarchical Clustering Portfolio

## 📌 Project Overview
This repository features a complete implementation of **Hierarchical Clustering** (specifically Agglomerative Clustering) applied to the famous Iris dataset. The project demonstrates how to build a tree-like hierarchy of clusters to understand data relationships.

---

## 🛠️ Algorithm Implemented: Hierarchical Clustering
- **Type**: Agglomerative (Bottom-Up) approach.
- **Dendrogram**: Used as a visual tool to decide the number of clusters by observing the longest vertical distance that doesn't intersect any horizontal line.
- **Linkage (Ward)**: This method focuses on minimizing the sum of squared differences within all clusters.



---

## 📊 Technical Workflow
1. **Standardization**: Preparing the features for distance-based calculations.
2. **Dendrogram Plotting**: Visualizing the hierarchical relationship between every data point.
3. **Model Fitting**: Training the `AgglomerativeClustering` model with the identified number of clusters.
4. **Evaluation**: Visualizing the resulting clusters in 2D space.

---

## ⚙️ Tech Stack
- **Language**: Python
- **Libraries**: 
  - `Scipy`: For creating the linkage matrix and dendrogram.
  - `Scikit-Learn`: For the clustering model.
  - `Pandas & NumPy`: For data manipulation.
  - `Matplotlib`: For cluster visualization.

---

## 📉 Key Insights
- Hierarchical clustering effectively identified the structural similarities in the Iris dataset.
- The Dendrogram provided a clear mathematical justification for selecting 3 clusters, which matches the actual number of species in the dataset.