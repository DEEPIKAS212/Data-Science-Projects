Portuguese Bank Marketing – Machine Learning Project
## Project Overview
This project focuses on predicting whether a customer will subscribe to a term deposit based on data from direct marketing campaigns conducted by a Portuguese banking institution.
The objective is to build a machine learning model that helps the bank marketing team identify potential customers, optimize campaigns, and reduce unnecessary outreach.
## Problem Statement
Banks conduct marketing campaigns via phone calls to promote term deposits. However, not all customers subscribe.
The goal of this project is to:
- Analyze customer data
- Build a predictive model
- Identify customers likely to subscribe (yes/no)
## Business Objective
- Improve marketing efficiency
- Reduce operational costs
- Target high-potential customers
- Increase conversion rates
## Dataset Information
Dataset Name: Portuguese Bank Marketing Dataset
File Used: bank-additional-full.csv
Records: 41,188
Features: 20 input features + 1 target variable
## Target Variable
y → Has the client subscribed to a term deposit?
yes → 1
no → 0
## Exploratory Data Analysis (EDA)
Checked dataset structure, data types, and distributions
Observed class imbalance (majority = 'no')
Analyzed key features like:
1. Age
2.Job
3. Campaign details
Economic indicators
## Key Insights
* Customers with previous successful campaigns are more likely to subscribe
* Higher number of contacts reduces success probability
* Call duration has strong influence (data leakage risk)
* Economic factors impact customer decisions
## Data Preprocessing
- Handled categorical features using One-Hot Encoding
- Scaled numerical features using StandardScaler
- Dropped duration feature to avoid data leakage
- No outlier removal (real-world meaningful data)
## Machine Learning Models Used
* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
## Model Evaluation Metrics
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
## Best Model
Gradient Boosting Classifier
**Performance:**
Accuracy: ~90%
ROC-AUC: ~0.80
Precision: Good
Recall: Moderate (expected due to imbalance)
## Business Recommendations
- Target customers with previous successful interactions
- Limit excessive contact attempts
- Focus on mobile-based communication
- Align campaigns with favorable economic conditions
- Prioritize specific customer segments (retired, students, professionals)
## Challenges Faced
Data Leakage: duration feature removed
Class Imbalance: Used ROC-AUC and F1-score for evaluation
High Cardinality Categorical Data: Handled using One-Hot Encoding
Model Selection: Avoided SVM due to computational cost
## Future Improvements
Apply SMOTE for class imbalance
Perform hyperparameter tuning
Optimize decision threshold
Deploy model using Flask or Streamlit
## Technologies Used
Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
## Conclusion
Built a complete end-to-end ML pipeline
Compared multiple classification models
Selected the best-performing model
Delivered actionable business insights
👩‍💻 Author
**Deepika S**
Aspiring Data Scientist | IT Enthusiast
