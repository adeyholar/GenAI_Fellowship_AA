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