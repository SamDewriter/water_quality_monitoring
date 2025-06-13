import pandas as pd

class SensorReading:
    """Class to model a sensor reading and evaluate its safety."""
    
    def __init__(self, sensor_id, location, ph, turbidity, temperature):
        """
        Initialize a sensor reading.
        
        Args:
            sensor_id (int): Sensor identifier.
            location (str): Location of the sensor.
            ph (float): pH value.
            turbidity (float): Turbidity value in NTU.
            temperature (float): Temperature in degrees Celsius.
        """
        self.sensor_id = sensor_id
        self.location = location
        self.ph = ph
        self.turbidity = turbidity
        self.temperature = temperature
        self.status = None
        self.reason = None
    
    def evaluate_safety(self):
        """
        Evaluate if the reading is safe based on pH and turbidity.
        
        Safe ranges:
            - pH: 6.5–8.5 (inclusive)
            - Turbidity: 0–1 NTU (inclusive)
        
        Returns:
            tuple: (bool, str) indicating (is_safe, reason).
        """
        is_safe = True
        reasons = []
        
        # Check pH
        if pd.isna(self.ph):
            is_safe = False
            reasons.append("missing pH")
        elif not (6.5 <= self.ph <= 8.5):
            is_safe = False
            reasons.append("pH too high" if self.ph > 8.5 else "pH too low")
        
        # Check turbidity
        if pd.isna(self.turbidity):
            is_safe = False
            reasons.append("missing turbidity")
        elif not (0 <= self.turbidity <= 1):
            is_safe = False
            reasons.append("turbidity too high")
        
        self.status = is_safe
        self.reason = ", ".join(reasons) if reasons else "Safe"
        
        return self.status, self.reason

class WaterQualityEvaluator:
    """Class to evaluate water quality for multiple sensor readings."""
    
    def __init__(self):
        self.readings = []
    
    def add_reading(self, sensor_id, location, ph, turbidity, temperature):
        """
        Add a sensor reading to the evaluator.
        
        Args:
            sensor_id (int): Sensor identifier.
            location (str): Location of the sensor.
            ph (float): pH value.
            turbidity (float): Turbidity value in NTU.
            temperature (float): Temperature in degrees Celsius.
        """
        reading = SensorReading(sensor_id, location, ph, turbidity, temperature)
        self.readings.append(reading)
    
    def evaluate_all(self):
        """
        Evaluate all sensor readings.
        
        Returns:
            list: List of tuples (sensor_id, location, is_safe, reason).
        """
        results = []
        for reading in self.readings:
            is_safe, reason = reading.evaluate_safety()
            results.append((reading.sensor_id, reading.location, is_safe, reason))
        return results
    
    def count_safety_status(self):
        """
        Count the number of safe and unsafe readings.
        
        Returns:
            tuple: (safe_count, unsafe_count)
        """
        safe_count = sum(1 for reading in self.readings if reading.status)
        unsafe_count = len(self.readings) - safe_count
        return safe_count, unsafe_count