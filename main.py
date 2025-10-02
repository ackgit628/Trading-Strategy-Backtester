from backtesting_engine.engine import BacktestingEngine
from strategies.example_strategy import ExampleStrategy
import pandas as pd

if __name__ == "__main__":
    # Placeholder: Load your data here
    data = pd.DataFrame()  # Replace with actual data loading

    strategy = ExampleStrategy()
    engine = BacktestingEngine(strategy, data)
    engine.run()
    engine.report()
