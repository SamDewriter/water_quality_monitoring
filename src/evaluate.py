class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_min, self.ph_max = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row):
        return self.ph_min <= row["pH"] <= self.ph_max and row["turbidity"] <= self.turbidity_threshold

    def evaluate(self, df):
        df = df.copy()
        df["is_safe"] = df.apply(self.is_safe, axis=1)
        return df
