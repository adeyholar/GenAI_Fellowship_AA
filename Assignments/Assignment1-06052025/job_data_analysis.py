import pandas as pd 

class Job_Data_Analysis:
    def __init__(self, csv_file):
        """Initialize with a CSV file and load it into a DataFrame."""
        try:
            self.df = pd.read_csv(csv_file)
        except FileNotFoundError:
            raise ValueError("CSV File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            raise ValueError("CSV File is empty. Please provide a valid CSV file.")
        except pd.errors.ParserError:
            raise ValueError("CSV File is malformed. Please check the file format.")
    
    def get_company_locations(self):
        """Return list of unique company locations."""
        return self.df['company_location'].unique().tolist()

    def get_salary_range_per_emp_type(self, country):
        """Return DataFrame with min, mean, max salary per employment type for a country."""
        filtered_df = self.df[self.df['company_location'] == country]
        if filtered_df.empty:
            return pd.DataFrame(columns=['employment_type', 'min', 'mean', 'max'])
        result = filtered_df.groupby('employment_type')['salary_usd'].agg(['min', 'mean', 'max']).reset_index()
        return result

    def get_avg_exp_per_level(self, country):
        """Return dict with average years of experience per experience level for a country."""
        filtered_df = self.df[self.df['company_location'] == country]
        if filtered_df.empty:
            return {}
        result = filtered_df.groupby('experience_level')['years_experience'].mean().to_dict()
        return result

    def get_num_industry(self):
        """Return dict with number of industries per country."""
        pass

    def get_benefit_score_range(self):
        """Return DataFrame with min, mean, max benefit score per country."""
        pass