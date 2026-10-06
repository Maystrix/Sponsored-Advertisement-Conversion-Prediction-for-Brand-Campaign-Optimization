# Sponsored-Advertisement-Conversion-Prediction-for-Brand-Campaign-Optimization
## Machine Learning-Based Binary Classification for E-Commerce Advertising ![rainbow](https://user-images.githubusercontent.com/102039796/216668803-7f6a97f1-9dff-419e-83e9-c4569092862c.png)

This project develops a machine learning classification pipeline to predict whether a user's interaction with a sponsored advertisement on an e-commerce platform will result in a product purchase (conversion).

The project covers the complete machine learning workflow — from exploratory data analysis and data preprocessing to baseline model comparison and hyperparameter tuning.

## 📌 <ins> **Project Overview:** </ins>

Sponsored advertising is an important component of modern e-commerce platforms. Predicting which advertisement interactions are likely to result in a purchase can help businesses better understand customer behavior and evaluate advertising effectiveness.

The objective of this project is to build a binary classification model that predicts:

- 1 → Conversion / Purchase
- 0 → No Conversion / No Purchase

Each record represents a sponsored advertisement interaction containing information related to the user, product, campaign, advertisement, engagement behavior, historical activity, and browsing context.

## 📊 <ins> **Dataset:** </ins>
- Records: 30,080
- Features: 34
- Categorical Features: 12
- Numerical Features: 21
- Target: conversion
- Class Distribution: 75.83% non-conversion, 24.17% conversion


## 🤖 <ins> **Models:** </ins>
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost
   
## <ins> **Best Baseline Result:** </ins>

XGBoost

<img width="800" height="350" alt="image" src="https://github.com/user-attachments/assets/d884c84d-3267-4846-b5ad-809476030481" />





## 🛠️ <ins> **Tech Stack:** </ins>

Python • Pandas • NumPy • Scikit-learn • XGBoost • Matplotlib • Seaborn • Jupyter Notebook


## 📈 <ins> **Key Findings:** </ins>
- A machine learning-based classification system was developed to predict whether a sponsored advertisement interaction will result in a purchase.
- The final Hyperparameter-Tuned XGBoost model achieved a test accuracy of **85.22%**, conversion precision of **74.58%**, conversion recall of **58.64%**, and conversion F1-score of **65.66%**.
- The model achieved a **ROC-AUC of 0.9072**, indicating strong discrimination between conversion and non-conversion cases.
- The model generates conversion probabilities that can help businesses identify high-, medium-, and low-potential advertising opportunities.
- These insights can support campaign optimization, prioritization of higher-conversion opportunities, and more informed advertising decisions.
  

## 🔄 Project Workflow

```text
Raw Dataset
    │
    ▼
Data Understanding
    │
    ▼
Exploratory Data Analysis
    │
    ├── Missing Values
    ├── Duplicates
    ├── Outliers
    ├── Distributions
    ├── Correlations
    └── Conversion Analysis
    │
    ▼
Data Preprocessing
    │
    ├── Duplicate Removal
    ├── Missing Value Imputation
    ├── Outlier Capping
    ├── Identifier Removal
    └── Categorical Encoding
    │
    ▼
Stratified Train-Test Split
    │
    ▼
Baseline Models
    │
    ├── Logistic Regression
    ├── Decision Tree
    ├── Random Forest
    └── XGBoost
    │
    ▼
Model Evaluation
    │
    ├── Accuracy
    ├── Precision
    ├── Recall
    ├── F1-Score
    └── ROC-AUC
    │
    ▼
Hyperparameter Tuning
    │
    ├── Random Forest
    └── XGBoost
    │
    ▼
Final Model Analysis
```



