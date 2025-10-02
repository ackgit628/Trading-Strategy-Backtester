import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers and time period
tickers = ['PEP', 'KO']  # PepsiCo and Coca-Cola
start_date = '2020-01-01'
end_date = '2025-01-01'

# Download the adjusted closing prices
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# Rename columns for clarity and drop any missing values
data.columns = ['pepsi', 'coke']
data = data.dropna()

# Save the data to CSV in the data directory
data.to_csv('data/pepsi_vs_coke.csv')

# Take a quick look at the data
print(data.head())

# Plot the price history
data.plot(figsize=(12, 6), title='Pepsi vs. Coca-Cola Price History')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price (USD)')
plt.show()
