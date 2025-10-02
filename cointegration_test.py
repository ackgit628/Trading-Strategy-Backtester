import yfinance as yf
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# --- Phase 1: Data Acquisition ---
tickers = ['PEP', 'KO']
start_date = '2020-01-01'
end_date = '2025-01-01'
# Download the closing prices
data = yf.download(tickers, start=start_date, end=end_date)['Close']
data.columns = ['pepsi', 'coke']
data = data.dropna()

# --- Phase 2: Cointegration Test ---
# Step 1: Run a linear regression to find the hedge ratio (beta)
# We add a constant to the regression model to account for a baseline offset
pepsi_with_const = sm.add_constant(data['pepsi'])
model = sm.OLS(data['coke'], pepsi_with_const)
results = model.fit()
# The hedge ratio is the coefficient of the 'pepsi' variable
beta = results.params['pepsi']
print(f"Hedge Ratio (Beta): {beta:.4f}")

# Step 2: Calculate the spread
spread = data['coke'] - beta * data['pepsi']

# Step 3: Run the Augmented Dickey-Fuller (ADF) test on the spread
adf_test = adfuller(spread, autolag='AIC')
print("\n--- ADF Test Results ---")
print(f"ADF Statistic: {adf_test[0]:.4f}")
p_value = adf_test[1]
print(f"P-value: {p_value:.4f}")

# Interpret the results
if p_value < 0.05:
    print("\nConclusion: The p-value is less than 0.05. The spread is likely stationary.")
    print("The pair PEP/KO is likely cointegrated. ✅")
else:
    print("\nConclusion: The p-value is greater than 0.05. The spread is likely non-stationary.")
    print("The pair PEP/KO is not a good candidate for this strategy. ❌")

# Plot the spread to visualize it
spread.plot(figsize=(12, 6), title='Coke-Pepsi Spread (Leash Distance)')
plt.axhline(spread.mean(), color='red', linestyle='--', label='Mean')
plt.ylabel('Spread Value')
plt.legend()
plt.show()
