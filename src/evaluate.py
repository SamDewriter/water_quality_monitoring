import pandas as pd
from typing import List, Tuple

class SensorReading:
    def __init__(self, sensor_id: str, location: str, ph: float, turbidity: float, temperature: float):
        self.sensor_id = sensor_id
        self.location = location
        self.ph = ph
        self.turbidity = turbidity
        self.temperature = temperature
        self.status: bool | None = None
        self.reason: str | None = None

    def evaluate_safety(self) -> Tuple[bool, str]:
        is_safe = True
        reasons: List[str] = []

        # Evaluate pH
        if pd.isna(self.ph):
            reasons.append("pH missing")
            is_safe = False
        elif self.ph < 6.5:
            reasons.append("pH too low")
            is_safe = False
        elif self.ph > 8.5:
            reasons.append("pH too high")
            is_safe = False

        # Evaluate turbidity
        if pd.isna(self.turbidity):
            reasons.append("turbidity missing")
            is_safe = False
        elif self.turbidity > 1:
            reasons.append("turbidity too high")
            is_safe = False

        self.status = is_safe
        self.reason = ", ".join(reasons) if reasons else "Safe"
        return self.status, self.reason


class WaterQualityEvaluator:
    def __init__(self):
        self.readings: List[SensorReading] = []

    def add_reading(self, sensor_id: str, location: str, ph: float, turbidity: float, temperature: float):
        self.readings.append(SensorReading(sensor_id, location, ph, turbidity, temperature))

    def evaluate_all(self) -> List[Tuple[str, str, bool, str]]:
        return [(r.sensor_id, r.location, *r.evaluate_safety()) for r in self.readings]

    def count_safety_status(self) -> Tuple[int, int]:
        # Ensure all readings have been evaluated
        for r in self.readings:
            if r.status is None:
                r.evaluate_safety()
        safe_count = sum(1 for r in self.readings if r.status)
        unsafe_count = len(self.readings) - safe_count
        return safe_count, unsafe_count

