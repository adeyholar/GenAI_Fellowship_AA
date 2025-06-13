import pandas as pd

# Sample stock market data with additional entries
data = {
    'Date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04', '2025-06-05',
             '2025-06-01', '2025-06-02', '2025-06-03'],
    'Stock': ['AAPL', 'AAPL', 'GOOG', 'GOOG', 'MSFT', 'MSFT', 'AAPL', 'GOOG'],
    'Price': [150.50, 152.75, 2750.00, 2780.25, 300.00, 305.00, 155.00, 2760.00],
    'Volume': [1000000, 1200000, 500000, 450000, 800000, 850000, 1100000, 480000]
}
df = pd.DataFrame(data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display original data
print("Original Stock Data:\n", df)

# Group by Stock and calculate mean price
grouped_by_stock = df.groupby('Stock')['Price'].mean()
print("\nAverage Price by Stock:\n", grouped_by_stock)

# Group by Date and sum Volume
grouped_by_date = df.groupby('Date')['Volume'].sum()
print("\nTotal Volume by Date:\n", grouped_by_date)

# Statistical analysis
stats = df['Price'].describe()
print("\nStatistical Summary of Prices:\n", stats)

# Group by Stock with multiple aggregations
grouped_stats = df.groupby('Stock').agg({'Price': ['mean', 'max', 'min'], 'Volume': 'sum'})
print("\nGrouped Statistics by Stock:\n", grouped_stats)