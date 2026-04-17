# Project Requirement — INX Future Inc Employee Performance
## Client Background
INX Future Inc is a leading data analytics and automation solutions provider
with 15+ years of global presence and 2,800+ employees across regions.
## Business Problem
* Employee performance indexes have declined over recent years
*  Client escalations have increased as a result
* Client satisfaction dropped by 8 points
* Management needs to identify root causes without impacting employee morale
## Business Questions to Answer
1. Which department has the best and worst performance?
2. What are the top factors affecting employee performance?
3. Can we build a model to predict employee performance rating?
4. How can this model assist pre-hiring and quarterly HR screening?
## Project Constraints
* Must not expose individual employee data publicly
* Predictions should assist HR decisions, not replace them
*  Model must be explainable to non-technical stakeholders
## Deliverables
* Cleaned dataset (Employee_Cleaned.csv)
* Trained model (best_model.pkl)
* Prediction notebook (predict_model.ipynb)
* Visualization dashboard (VIZ_01 to VIZ_04)
* Final summary with business recommendations
## Input Data
* Source: INX_Employee_Data.xlsx
* Rows: 1,200 employees
* Columns: 28 features including demographics, job details, satisfaction scores
* Target Variable: PerformanceRating (2 = Low, 3 = Good, 4 = Excellent)