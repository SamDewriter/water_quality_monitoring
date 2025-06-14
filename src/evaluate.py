import pandas as pd

class SensorReading:
    def __init__(self, sensor_id, location, ph, turbidity, temperature):
        self.sensor_id = sensor_id
        self.location = location
        self.ph = ph
        self.turbidity = turbidity
        self.temperature = temperature
        self.status = None
        self.reason = None

    def evaluate_safety(self):
        is_safe = True
        reasons = []

        if pd.isna(self.ph):
            is_safe = False
            reasons.append("pH missing")
        elif self.ph < 6.5:
            is_safe = False
            reasons.append("pH too low")
        elif self.ph > 8.5:
            is_safe = False
            reasons.append("pH too high")

        if pd.isna(self.turbidity):
            is_safe = False
            reasons.append("turbidity missing")
        elif self.turbidity > 1:
            is_safe = False
            reasons.append("turbidity too high")

        self.status = is_safe
        self.reason = ", ".join(reasons) if reasons else "Safe"

        return self.status, self.reason


class WaterQualityEvaluator:
    def __init__(self):
        self.readings = []

    def add_reading(self, sensor_id, location, ph, turbidity, temperature):
        reading = SensorReading(sensor_id, location, ph, turbidity, temperature)
        self.readings.append(reading)

    def evaluate_all(self):
        return [
            (r.sensor_id, r.location, *r.evaluate_safety())
            for r in self.readings
        ]

    def count_safety_status(self):
        safe_count = sum(1 for r in self.readings if r.status)
        return safe_count, len(self.readings) - safe_count
