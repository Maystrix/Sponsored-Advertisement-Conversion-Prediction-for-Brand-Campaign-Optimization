# Sponsored-Advertisement-Conversion-Prediction-for-Brand-Campaign-Optimization
### Machine Learning-Based Binary Classification for E-Commerce Advertising ![rainbow](https://user-images.githubusercontent.com/102039796/216668803-7f6a97f1-9dff-419e-83e9-c4569092862c.png)

This project develops a machine learning classification pipeline to predict whether a user's interaction with a sponsored advertisement on an e-commerce platform will result in a product purchase (conversion).

The project covers the complete machine learning workflow — from exploratory data analysis and data preprocessing to baseline model comparison and hyperparameter tuning.

📌 <u> **Project Overview:** </u>

Sponsored advertising is an important component of modern e-commerce platforms. Predicting which advertisement interactions are likely to result in a purchase can help businesses better understand customer behavior and evaluate advertising effectiveness.

The objective of this project is to build a binary classification model that predicts:

1 → Conversion / Purchase
0 → No Conversion / No Purchase

Each record represents a sponsored advertisement interaction containing information related to the user, product, campaign, advertisement, engagement behavior, historical activity, and browsing context.

📊 Dataset

The dataset initially contains:

Characteristic	Value
Records	30,080
Columns	34
Categorical Features	12
Numerical Features	21
Initial Duplicate Records	80
Target Variable	conversion
Non-Conversion	75.83%
Conversion	24.17%

The dataset is moderately imbalanced, making metrics such as Precision, Recall, F1-Score, and ROC-AUC particularly important alongside Accuracy.

🔍 Exploratory Data Analysis

The EDA process examined:

Dataset structure
Missing values
Duplicate records
Target distribution
Numerical feature distributions
Outliers
Feature correlations
Categorical conversion rates

Some notable relationships identified during EDA include:

time_on_ad_seconds ↔ time_on_page_seconds: 0.85
clicks ↔ impressions: 0.65
clicks ↔ click_through_rate: 0.67

Conversion rates also varied across campaign type, ad position, target audience, and user segment.

🛠️ Data Preprocessing

The following preprocessing pipeline was implemented:

Duplicate Removal
Removed 80 duplicate records.
Target Separation
Separated conversion from the feature set.
Train-Test Split
80% training data
20% testing data
Stratified split
random_state=42
Missing Value Treatment
Numerical missing values were imputed using training-set medians.
Outlier Treatment
IQR-based capping was applied to seven numerical features.
Identifier Removal
Removed:
user_id
campaign_id
ad_id
Categorical Encoding
income_level → Ordinal Encoding
Remaining categorical variables → One-Hot Encoding
Feature Alignment
Training and testing feature columns were aligned after encoding.

The preprocessing was designed to avoid data leakage by calculating imputation and outlier-treatment statistics from the training data before applying them to the test data.

🤖 Machine Learning Models

Four classification algorithms were evaluated:

Logistic Regression
Decision Tree
Random Forest
XGBoost
Baseline Model Performance
Model	Test F1	Test ROC-AUC	Test Recall	Test Precision
Logistic Regression	0.590	0.837	0.769	0.478
Decision Tree	0.514	0.680	—	—
Random Forest	0.629	0.881	—	—
XGBoost	0.685	0.903	0.797	0.601

Among the baseline models, XGBoost achieved the strongest reported F1-score and ROC-AUC.

⚙️ Hyperparameter Tuning
Random Forest

Random Forest was tuned using:

GridSearchCV
5-fold StratifiedKFold
F1-score as the optimization metric
48 parameter combinations
240 total fits

Best parameters:

n_estimators = 200
max_depth = 15
min_samples_split = 5
min_samples_leaf = 2
max_features = sqrt

Best cross-validation F1-score: 0.6664

Tuned test performance:

Metric	Score
Accuracy	0.8232
Precision	0.6195
Recall	0.6902
F1-Score	0.6529
ROC-AUC	0.8835

XGBoost

XGBoost tuning used:

GridSearchCV
5-fold StratifiedKFold
F1-score as the optimization metric
32 parameter combinations
160 total fits

Best parameters:

n_estimators = 200
max_depth = 3
learning_rate = 0.1
min_child_weight = 3
subsample = 1.0

Best cross-validation F1-score: 0.6681

Tuned test performance:

Metric	Score
Accuracy	0.8522
Precision	0.7458
Recall	0.5864
F1-Score	0.6566
ROC-AUC	0.9072

An important finding is that tuning did not automatically improve every metric. The tuned XGBoost model improved precision and ROC-AUC, but its test F1-score was lower than the untuned XGBoost baseline.

📈 Key Findings
- XGBoost provided the strongest baseline F1-score (0.685).
- XGBoost achieved the strongest baseline ROC-AUC (0.903).
- The tuned XGBoost model achieved a ROC-AUC of 0.9072.
- Logistic Regression provided relatively high recall but lower precision.
- Decision Tree showed evidence of overfitting and comparatively weaker performance.
- Random Forest performed better than Logistic Regression and Decision Tree but still showed a train-test performance gap.
- Hyperparameter tuning changed the precision-recall trade-off rather than universally improving all metrics.
- Model evaluation should therefore consider the business objective and appropriate metric, rather than relying only on Accuracy.
  
🔄 Machine Learning Workflow
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
🧰 Technologies & Tools
Python
Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn
XGBoost
Jupyter Notebook
Excel
