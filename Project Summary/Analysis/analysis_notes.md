# Analysis Notes — INX Future Inc Employee Performance
## Methodology Choices
### Why Random Forest?
* Highest accuracy (93.75%) among 6 models tested
* Built-in feature importance for business interpretation
*  Robust to outliers and skewed distributions
*  No need for feature scaling
*  Handles class imbalance better than single trees
### Models Compared
| Model | Accuracy | Notes |
|-------|----------|-------|
| Random Forest | 93.75% | Selected as final model |
| Gradient Boosting | ~91% | Good but slower to train |
| Decision Tree | ~88% | Fast but prone to overfitting |
| SVM | ~85% | Requires scaled features |
| Logistic Regression | ~76% | Linear — limited for this task |
| KNN | ~72% | Sensitive to feature scale |
### Preprocessing Decisions
*  Label Encoding used for categorical columns (not One-Hot) — tree models handle ordinal encoding well
*  Class weights balanced during training due to imbalance (Low: 16%, Good: 73%, Excellent: 11%)
* 80/20 train-test split with stratify=y to preserve class ratios
* No feature scaling applied — Random Forest doesn't require it
### EDA Key Findings
| Finding | Detail |
|---------|--------|
| Best dept | Development (avg 3.09, only 3.6% low performers) |
| Worst dept | Finance (avg 2.78, 30.6% low performers) |
| #1 factor | EmpEnvironmentSatisfaction — Rating 2 avg: 1.58, Rating 4 avg: 3.08 |
| #2 factor | EmpLastSalaryHikePercent — Rating 4 avg: 20.7% vs Rating 2: 15.1% |
| #3 factor | YearsSinceLastPromotion — Low performers: 3.7 yrs, Good performers: 1.9 yrs |
| Gender | No significant difference — Male: 2.95, Female: 2.95 |
| Overtime | Minimal impact on performance |
### Feature Insights
| Feature | Insight |
|---------|---------|
| Age | No strong separation — Low and Good performers spread across all ages equally |
| TotalWorkExperience | Excellent performers tend to have slightly more experience, but overlap is high |
| ExperienceAtCompany | Similar distribution across ratings — tenure alone doesn't predict performance |
| DistanceFromHome | No clear pattern — commute distance doesn't affect performance |
| EmpHourlyRate | Very similar distributions — pay rate alone doesn't separate performance levels |
| YearsSinceLastPromotion | Clear separation — Low performers cluster at higher values (longer gaps) |