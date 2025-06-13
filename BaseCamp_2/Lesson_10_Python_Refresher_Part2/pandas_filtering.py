import pandas as pd

# Sample stock market data
data = {
    'Date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04', '2025-06-05'],
    'Stock': ['AAPL', 'AAPL', 'GOOG', 'GOOG', 'MSFT'],
    'Price': [150.50, 152.75, 2750.00, 2780.25, 300.00],
    'Volume': [1000000, 1200000, 500000, 450000, 800000]
}
df = pd.DataFrame(data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display original data
print("Original Stock Data:\n", df)

# Simple filter: Price > 1000
high_price = df[df['Price'] > 1000]
print("\nStocks with Price > $1000:\n", high_price)

# Complex condition: Price > 1000 and Volume < 600000
complex_filter = df[(df['Price'] > 1000) & (df['Volume'] < 600000)]
print("\nStocks with Price > $1000 and Volume < 600,000:\n", complex_filter)

# Filter by Stock and Date range
recent_high = df[(df['Stock'] == 'GOOG') & (df['Date'] >= '2025-06-03')]
print("\nRecent GOOG stocks (from June 3):\n", recent_high)