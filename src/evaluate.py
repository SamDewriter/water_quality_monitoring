import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        
        Args:
            row (pd.Series): A row of sensor data.

        Returns:
            bool: True if safe, False otherwise.
        """
        if pd.isna(row['ph']) or pd.isna(row['turbidity']):
            return False
        if not (self.ph_range[0] <= row['ph'] <= self.ph_range[1]):
            return False
        if row['turbidity'] > self.turbidity_threshold:
            return False
        return True

    def get_reason(self, row: pd.Series) -> str:
        """
        Provide reason for safety status of the sensor data row.
        
        Args:
            row (pd.Series): A row of sensor data.

        Returns:
            str: Reason message including emoji.
        """
        if pd.isna(row['ph']):
            return "❌ Unsafe (missing pH)"
        if pd.isna(row['turbidity']):
            return "❌ Unsafe (missing turbidity)"
        if row['ph'] < self.ph_range[0]:
            return "❌ Unsafe (pH too low)"
        if row['ph'] > self.ph_range[1]:
            return "❌ Unsafe (pH too high)"
        if row['turbidity'] > self.turbidity_threshold:
            return "❌ Unsafe (turbidity too high)"
        return "✅ Safe"
