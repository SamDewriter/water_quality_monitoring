import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        """
        column_metric = row.name

        # False if value is missing on pH or turbidity
        if row.isna().any():
            return False

        if column_metric == "pH":
            return ((row < 6.5) | (row > 8.5)).any()

        if column_metric == "turbidity":
            return (row < 1).any()
