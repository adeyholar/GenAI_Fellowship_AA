import pandas as pd

# Sample stock market data (simulating 2,800+ records with a smaller set)
data = {
    'Date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04', '2025-06-05'],
    'Stock': ['AAPL', 'AAPL', 'GOOG', 'GOOG', 'MSFT'],
    'Price': [150.50, 152.75, 2750.00, 2780.25, 300.00],
    'Volume': [1000000, 1200000, 500000, 450000, 800000]
}
df = pd.DataFrame(data)

# Display the dataframe
print("Stock Market Data:\n", df)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
print("\nData with datetime:\n", df)

# Basic analysis
average_price = df['Price'].mean()
total_volume = df['Volume'].sum()
print(f"\nAverage Price: ${average_price:.2f}")
print(f"Total Volume: {total_volume:,}")

# Filtering data
high_price_stocks = df[df['Price'] > 1000]
print("\nStocks with price > $1000:\n", high_price_stocks)