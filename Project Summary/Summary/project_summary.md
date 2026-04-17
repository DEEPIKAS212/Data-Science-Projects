# Project Summary — INX Future Inc Employee Performance
## Objective
Identify root causes of declining employee performance and build a
predictive model to assist HR in hiring and quarterly monitoring decisions.
## Key Results
| Business Question | Answer |
|-------------------|--------|
| Best performing department | Development (avg 3.09) |
| Worst performing department | Finance (avg 2.78, 30.6% low performers) |
| #1 performance factor | Salary Hike % (21.3% importance) |
| #2 performance factor | Environment Satisfaction (20.1% importance) |
| #3 performance factor | Years Since Last Promotion (9.8% importance) |
| Best ML model | Random Forest — 93.75% accuracy |
| Employees at risk (predicted Low) | 190 out of 1,200 |
## Top 3 Actionable Recommendations
### 1. Fix Environment Satisfaction in Finance & Sales
- Finance avg environment satisfaction is critically low
- Run quarterly anonymous surveys
- Act on results within 30 days of survey close
### 2. Review Salary Hike Policy
- Low performers receive avg 15.1% hike vs 20.7% for Excellent performers
- Hike differentiation should be wider to incentivize performance
- Consider performance-linked hike bands
### 3. Reduce Promotion Gaps
- Low performers average 3.7 years since last promotion
- Good performers average 1.9 years
- Flag any employee with 3+ years without promotion for a career review
## Model Summary
- Algorithm: Random Forest Classifier
- Accuracy: 93.75%
- Features used: 26
- Training set: 960 employees
- Test set: 240 employees
- Predicted Low performers in full dataset: 190 employees
## Non-Influential Factors
The following factors were found to have no meaningful impact on performance:
- Gender (Male: 2.95, Female: 2.95 — identical)
- Marital Status (max difference: 0.06 points)
- Overtime (proportions nearly identical across ratings)
- Distance From Home
- Age