import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        """
        if pd.isna(row.get("pH")) or pd.isna(row.get("turbidity")):
            return False

        return (
            self.ph_range[0] <= row["pH"] <= self.ph_range[1]
            and row["turbidity"] <= self.turbidity_threshold
        )

    def evaluate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Evaluate safety of each row and return a DataFrame with results.
        """
        results = []

        for i, row in df.iterrows():
            location = row.get("location") if pd.notna(row.get("location")) else "Unknown"
            sensor_label = f"Sensor {i + 1} at {location}"
            status = " Safe" if self.is_safe(row) else " Unsafe"
            results.append({"sensor": sensor_label, "status": status})

        results_df = pd.DataFrame(results)
        return results_df



