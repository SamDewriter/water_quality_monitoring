import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_min, self.ph_max = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        Returns True if both pH and turbidity are within safe limits.
        """
        ph = row['pH']
        turb = row['turbidity']
        return self.ph_min <= ph <= self.ph_max and turb <= self.turbidity_threshold

    def evaluate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Adds 'ph_status', 'turbidity_status', and 'overall_safety' columns to the DataFrame.
        """
        df = df.copy()

        df["ph_status"] = df["pH"].apply(lambda x: "✅ Normal" if self.ph_min <= x <= self.ph_max else "⚠️ Out of Range")
        df["turbidity_status"] = df["turbidity"].apply(lambda x: "✅ Normal" if x <= self.turbidity_threshold else "⚠️ High Turbidity")
        df["overall_safety"] = df.apply(self.is_safe, axis=1)

        return df
