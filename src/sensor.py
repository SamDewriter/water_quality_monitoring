# sensor.py
class SensorReading:
    def __init__(self, sensor_id, location, ph, turbidity):
        self.sensor_id = sensor_id
        self.location = location or "Unknown location"
        self.ph = ph
        self.turbidity = turbidity
        self.safety_status = None

    def to_dict(self):
        return {
            "sensor_id": self.sensor_id,
            "location": self.location,
            "ph": self.ph,
            "turbidity": self.turbidity,
            "safety_status": self.safety_status
        }
