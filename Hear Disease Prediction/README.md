**Heart Disease Prediction using Machine Learning**
## Project Overview
Heart disease is one of the leading causes of death worldwide. Early identification of individuals at risk can significantly reduce life-threatening complications.
This project focuses on building a machine learning model to predict whether a person is likely to have heart disease based on clinical and medical attributes. The model is designed as a risk prediction and decision-support tool, not as a medical diagnostic system.
## Objectives
- Perform detailed Exploratory Data Analysis (EDA) to understand patient health patterns
- Build and compare multiple machine learning models
- Predict the likelihood of heart disease (binary classification)
- Provide actionable insights to support early screening in healthcare
## Dataset Description
The dataset contains patient medical attributes such as:
1. Age
2. Sex
3. Chest pain type
4. Resting blood pressure
5.Serum cholesterol
6.Fasting blood sugar
7.Resting ECG results
8.Maximum heart rate achieved
9.Exercise-induced angina
10.ST depression (oldpeak)
11.Slope of ST segment
12.Number of major vessels
T13.halassemia
## Target Variable
0 → No Heart Disease
1 → Heart Disease Present
## Exploratory Data Analysis (EDA)
* Dataset is clean (no missing or duplicate values)
* Mild class imbalance handled using stratified sampling
* Features like chest pain type, thalassemia, oldpeak, and max heart rate show strong correlation with heart disease
* Outliers were identified but retained to preserve clinical significance
* Low multicollinearity observed among features
## Data Preprocessing
- Numerical Features → Standard Scaling
- Categorical Features → One-Hot Encoding
- Implemented using:
- Pipeline
- ColumnTransformer
- Ensured no data leakage during training
## Machine Learning Models Used
`1.Logistic Regression
2.Random Forest Classifier
3.XGBoost Classifier
4.Support Vector Machine (SVM)
## Model Optimization
1.Hyperparameter tuning using GridSearchCV
2.Stratified K-Fold Cross Validation
## Model Evaluation Metrics
* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC Score
## Final Model Selection
- Both Random Forest and XGBoost achieved similar performance.
- Random Forest was selected as the final model because:
- Better interpretability
- Robust performance on small datasets
- Provides meaningful feature importance
- Suitable for healthcare decision-support
## High recall was prioritized to minimize false negatives, as missing a heart disease case can be critical.
**Key Insights**
- Higher ST depression (oldpeak) is strongly associated with heart disease
- Abnormal thalassemia values indicate higher risk
- Exercise-related features are significant predictors
- Patients with heart disease show greater variability in clinical measurements
## Suggestions for Healthcare Use
* Can be used as an early screening tool to identify high-risk patients
* Helps in prioritizing patients for further medical evaluation
* Supports doctors in decision-making, not replaces them
* Enables preventive care and timely intervention
## Limitations
- Small dataset size (180 samples)
- Model performance may vary on larger or real-world datasets
- Not a substitute for professional medical diagnosis
## Future Scope
* Use larger and more diverse datasets
* Apply advanced feature engineering
* Implement cost-sensitive learning
* Deploy as a real-time clinical decision support system
* Integrate with hospital data systems
## Technologies Used
1.Python
2.NumPy
3.Pandas
4.Matplotlib & Seaborn
5.Scikit-learn
6.XGBoost
## Conclusion
This project demonstrates how machine learning can assist in early risk prediction of heart disease. By focusing on interpretability and recall, the model provides a reliable approach for supporting healthcare professionals in identifying high-risk individuals and reducing potential life-threatening conditions.
👩‍💻 Author
**Deepika S**
**Data Scientist | IT Enthusiast**
