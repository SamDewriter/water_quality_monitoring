import pandas as pd
from evaluate import WaterQualityEvaluator
class Sensor:
    def __init__(self, sensor_id: str, readings: pd.DataFrame):
        self.sensor_id = sensor_id
        self.readings = readings
        self.location = self.readings['location'].unique()[0]
        self.water_quality_evaluator = WaterQualityEvaluator()
        self.status = '✅ Safe' if self.is_safe() == True else '❌ Unsafe'

    def is_safe(self):
        return self.water_quality_evaluator.is_safe(self.readings['pH']) & self.water_quality_evaluator.is_safe(self.readings['turbidity'])

    def summary(self):
        return f"Sensor {self.sensor_id} at Lake {self.location}: {self.status}"
