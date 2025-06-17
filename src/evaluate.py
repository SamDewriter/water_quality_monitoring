import pandas as pd
# evaluate.py
class WaterQualityEvaluator:
    def __init__(self, ph_min: float, ph_max: float, turbidity_max: float):
        self.ph_min = ph_min
        self.ph_max = ph_max
        self.turbidity_max = turbidity_max

    def evaluate(self, sensor):
        reasons = []

        if sensor.ph is None or pd.isna(sensor.ph):
            reasons.append("missing pH")
        elif not (self.ph_min <= sensor.ph <= self.ph_max):
            reasons.append("pH too high" if sensor.ph > self.ph_max else "pH too low")

        if sensor.turbidity is None or pd.isna(sensor.turbidity):
            reasons.append("missing turbidity")
        elif sensor.turbidity > self.turbidity_max:
            reasons.append("turbidity too high")

        sensor.safety_status = f"Unsafe ({', '.join(reasons)})" if reasons else "Safe"
        return sensor


