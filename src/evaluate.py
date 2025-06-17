import  pandas as pd
class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        """
ph_ok = self.ph_range[0] <= row['pH'] <= self.ph_range[1]
turbidity_ok = row['turbidity'] <= self.turbidity_threshold
return ph_ok and turbidity_ok
