# INX Future Inc — Employee Performance Analysis # 
### IABAC CDS Project 1
## Project Overview
INX Future Inc is a leading data analytics and automation solutions provider with 15+ years of global presence. Recent employee performance indexes have declined, leading to increased client escalations and an 8-point drop in client satisfaction. This project identifies root causes using data science and builds a predictive model to assist hiring decisions.
## Directory Structure
INX_Employee_Performance/
│
├── Project_Summary/
│   ├── Requirement/     ← Project brief and business questions
│   └── Analysis/        ← Analysis notes
│   └── Summary/         
│
├── data/
│   ├── raw/src/         ← Original, unmodified dataset (INX_Employee_Data.xlsx)
│   ├── processed/       ← Cleaned CSV + all generated charts
│   └── external/        ← (Reserved for external reference data)
│
├── src/
│   ├── Data_Processing/
│   │   ├── data_processing.ipynb           ← Step 1: Clean & encode data
│   │   └── data_exploratory_analysis.ipynb ← Step 2: EDA & department insights
│   │
│   ├── models/
│   │   ├── train_model.ipynb   ← Step 3: Train & compare ML models
│   │   └── predict_model.ipynb ← Step 4: Use model for predictions
│   │
│   └── visualization/
│       └── visualize.ipynb     ← Step 5: Final business charts
│
├── references/
│   └── data_dictionary.md      ← Column descriptions
│
└── README.md                   ← This file

## How to Run (Step by Step)
> Run notebooks **in order**. Each notebook's output feeds the next.
### Step 1 — Data Processing
Open: src/Data_Processing/data_processing.ipynb
Run all cells
Output: data/processed/INX_Employee_Cleaned.csv
### Step 2 — Exploratory Data Analysis
Open: src/Data_Processing/data_exploratory_analysis.ipynb
Run all cells
Output: Charts fig_01 to fig_08 in data/processed/
### Step 3 — Train Model
Open: src/models/train_model.ipynb
Run all cells
Output: src/models/best_model.pkl  +  fig_09 to fig_11
### Step 4 — Predict
Open: src/models/predict_model.ipynb
Run all cells
Output: data/processed/INX_Employee_Predictions.csv
### Step 5 — Visualizations
Open: src/visualization/visualize.ipynb
Run all cells
Output: VIZ_01 to VIZ_04 charts in data/processed/
## Key Results
| Business Question | Answer |
|-------------------|--------|
| Best performing department | Development (avg 3.09) |
| Worst performing department | Finance (avg 2.78, 30.6% low performers) |
| #1 factor | Salary Hike % (21.3% importance) |
| #2 factor | Environment Satisfaction (20.1% importance) |
| #3 factor | Years Since Last Promotion (9.8% importance) |
| Best ML model | Random Forest — 93.75% accuracy |
## Requirements
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl shap
## Methodology
1. Data Cleaning: Missing value handling, outlier capping
2. Feature Engineering: Encoding, transformation
3. Model Training: Multiple models with cross-validation
4. Evaluation: Accuracy, F1-score, Confusion Matrix
5. Selection: Best model based on performance & stability
