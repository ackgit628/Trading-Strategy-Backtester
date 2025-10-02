import pandas as pd

class ExampleStrategy:
    def __init__(self, params=None):
        self.params = params or {}

    def apply(self, data: pd.DataFrame):
        # Placeholder for strategy logic
        print("Applying example strategy...")
        return data
