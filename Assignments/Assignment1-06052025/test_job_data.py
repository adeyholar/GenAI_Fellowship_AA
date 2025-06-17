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
        print("\nUnique company locations:")
        print(analysis.get_company_locations())
        print(len(analysis.get_company_locations()), "unique company locations found.")
        print("\nSalary range for United States:")
        print(analysis.get_salary_range_per_emp_type('United States'))
        print("\nSalary range for InvalidCountry:")
        print(analysis.get_salary_range_per_emp_type('InvalidCountry'))
        print("\nAverage experience per level for United States:")
        print(analysis.get_avg_exp_per_level('United States'))
        print("\nAverage experience per level for InvalidCountry:")
        print(analysis.get_avg_exp_per_level('InvalidCountry'))
        print("\nNumber of industries per country:")
        print(analysis.get_num_industry())
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)