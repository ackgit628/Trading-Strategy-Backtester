
# Trading Strategy Backtester

A Python project for backtesting pairs trading strategies. This project provides scripts for data acquisition, cointegration testing, signal generation, and stop-loss logic, along with a modular structure for custom strategies and backtesting.

## Project Structure
- `strategies/` — Custom trading strategies
- `data/` — Market data files (CSV, etc.)
- `backtesting_engine/` — Core backtesting logic
- `results/` — Output and performance reports
- `get_data.py` — Script to download and save historical price data
- `cointegration_test.py` — Script to test for cointegration between asset pairs
- `generate_signals.py` — Script to generate trading signals based on Z-score
- `generate_signals_with_stoploss.py` — Script to generate signals with stop-loss logic

## Getting Started
1. Install dependencies:
	```sh
	pip install -r requirements.txt
	```
2. Download historical data:
	```sh
	python get_data.py
	```
	This will save a CSV in the `data/` directory.
3. Test for cointegration:
	```sh
	python cointegration_test.py
	```
4. Generate trading signals:
	```sh
	python generate_signals.py
	```
5. Generate signals with stop-loss:
	```sh
	python generate_signals_with_stoploss.py
	```

## Usage
- Edit the scripts to change tickers, dates, or parameters as needed.
- Plots and results will be shown in the terminal or as pop-up windows.
- Output data and plots can be saved to the `data/` or `results/` folders as needed.

## Requirements
See `requirements.txt` for dependencies.
