import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# --- Phases 1 & 2: Data and Cointegration ---
tickers = ['EWA', 'EWC']
start_date = '2020-01-01'
end_date = '2024-12-31'
data = yf.download(tickers, start=start_date, end=end_date)['Close']
data.columns = ['australia_etf', 'canada_etf']
data = data.dropna()

australia_with_const = sm.add_constant(data['australia_etf'])
model = sm.OLS(data['canada_etf'], australia_with_const)
results = model.fit()
beta = results.params['australia_etf']
spread = data['canada_etf'] - beta * data['australia_etf']
data['spread'] = spread

# --- Phase 3: Signal Generation ---
# 1. Calculate the Z-score
# We use a 30-day rolling window to calculate the mean and standard deviation.
data['rolling_mean'] = data['spread'].rolling(window=30).mean()
data['rolling_std'] = data['spread'].rolling(window=30).std()
data['z_score'] = (data['spread'] - data['rolling_mean']) / data['rolling_std']

# 2. Define trading thresholds
upper_threshold = 1.5
lower_threshold = -1.5

# 3. Create signals
data['signal'] = 0
# Signal to go short the spread
data.loc[data['z_score'] > upper_threshold, 'signal'] = -1
# Signal to go long the spread
data.loc[data['z_score'] < lower_threshold, 'signal'] = 1

# 4. Create position
# The position is the signal, forward-filled. We are either long (+1), short (-1), or flat (0).
# We also add logic to exit when the z-score crosses the mean (0).
data['position'] = data['signal'].replace(0, method='ffill')
# Exit condition: If in a position and z-score crosses the mean, exit (position = 0)
data.loc[(data['position'] == 1) & (data['z_score'] > 0), 'position'] = 0
data.loc[(data['position'] == -1) & (data['z_score'] < 0), 'position'] = 0
# Forward-fill the exit signals to hold the flat position
data['position'] = data['position'].replace(0, method='ffill').fillna(0)

# Print the tail of the DataFrame to see the new columns
print("\n--- Data with Z-Score and Positions ---")
print(data.tail(10))

# Plot the Z-score and thresholds
data['z_score'].plot(figsize=(14, 7), title='Spread Z-Score')
plt.axhline(upper_threshold, color='red', linestyle='--', label='Upper Threshold')
plt.axhline(lower_threshold, color='green', linestyle='--', label='Lower Threshold')
plt.axhline(0, color='black', linestyle='-')
plt.legend()
plt.show()
