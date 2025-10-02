import yfinance as yf
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# --- Phase 1: Data Acquisition ---
tickers = ['EWA', 'EWC']  # Australia and Canada ETFs
start_date = '2020-01-01'
end_date = '2024-12-31'
# Download the closing prices
data = yf.download(tickers, start=start_date, end=end_date)['Close']
data.columns = ['stock1', 'stock2']
data = data.dropna()

# --- Phase 2: Cointegration Test ---
# Step 1: Run a linear regression to find the hedge ratio (beta)
# We add a constant to the regression model to account for a baseline offset
stock1_with_const = sm.add_constant(data['stock1'])
model = sm.OLS(data['stock2'], stock1_with_const)
results = model.fit()
# The hedge ratio is the coefficient of the 'stock1' variable
beta = results.params['stock1']
print(f"Hedge Ratio (Beta): {beta:.4f}")

# Step 2: Calculate the spread
spread = data['stock2'] - beta * data['stock1']

# Step 3: Run the Augmented Dickey-Fuller (ADF) test on the spread
adf_test = adfuller(spread, autolag='AIC')
print("\n--- ADF Test Results ---")
print(f"ADF Statistic: {adf_test[0]:.4f}")
p_value = adf_test[1]
print(f"P-value: {p_value:.4f}")

# Interpret the results
if p_value < 0.05:
    print("\nConclusion: The p-value is less than 0.05. The spread is likely stationary.")
    print("The pair EWA/EWC is likely cointegrated. ✅")
else:
    print("\nConclusion: The p-value is greater than 0.05. The spread is likely non-stationary.")
    print("The pair EWA/EWC is not a good candidate for this strategy. ❌")

# Plot the spread to visualize it
spread.plot(figsize=(12, 6), title='Australia - Canada ETF Spread (Leash Distance)')
plt.axhline(spread.mean(), color='red', linestyle='--', label='Mean')
plt.ylabel('Spread Value')
plt.legend()
plt.show()
