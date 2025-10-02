import pandas as pd

class BacktestingEngine:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
        self.results = None

    def run(self):
        # Placeholder for backtesting logic
        print("Running backtest...")
        # Example: self.results = self.strategy.apply(self.data)
        pass

    def report(self):
        # Placeholder for reporting logic
        print("Generating report...")
        pass
