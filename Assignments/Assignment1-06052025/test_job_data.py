import pandas as pd
from job_data_analysis import Job_Data_Analysis
if __name__ == "__main__":
    import sys
    import os
    csv_path = os.path.join(os.path.dirname(__file__), 'ai_job_dataset.csv')
    try:
        analysis = Job_Data_Analysis(csv_path)
        print("DataFrame loaded successfully!")
        print("\nFirst 5 rows:")
        print(analysis.df.head())
        print("\nColumns:")
        print(analysis.df.columns)
        print(f"\nNumber of rows: {len(analysis.df)}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)