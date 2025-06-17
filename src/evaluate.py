import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        """
        reasons= []
        if pd.isna(row["pH"]):
            reasons.append("Missing pH")
        elif row["pH"] < self.ph_range[0]:
            reasons.append("pH too low")
        elif row["pH"] > self.ph_range[1]:
            reasons.append("pH too high")

        if pd.isna(row["turbidity"]):
            reasons.append("missing turbidity")
        elif row["turbidity"] > self.turbidity_threshold:
            reasons.append("turbidity too high")

        return (len(reasons) == 0, reasons)
