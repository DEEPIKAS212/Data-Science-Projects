from pathlib import Path                    # ← capital P
BASE        = Path(__file__).resolve().parent
RAW_DATA    = BASE / 'data' / 'raw' / 'src' / 'INX_Employee_Data.xlsx'
CLEANED     = BASE / 'data' / 'processed' / 'Employee_Cleaned.csv'
PREDICTIONS = BASE / 'data' / 'processed' / 'Employee_Predictions.csv'
MODEL       = BASE / 'models' / 'best_model.pkl'