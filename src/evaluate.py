import pandas as pd
class WaterQualityEvaluator:
    """
    A class to evaluate water quality based on pH and turbidity thresholds.
    """
    def __init__(self, ph_min=6.5, ph_max=8.5, turbidity_max=1.0):
        """
        Initialize with safe thresholds for pH & turbidity.
        
        Args:
            ph_min (float): Minimum safe pH value (default: 6.5).
            ph_max (float): Maximum safe pH value (default: 8.5).
            turbidity_max (float): Maximum safe turbidity value (default: 1.0).
        """

        self.ph_min = ph_min
        self.ph_max = ph_max
        self.turbidity_max = turbidity_max
    
    def evaluate_row(self, row):
        """
        Evaluate a single row of sensor data for water safety.
        
        Args:
            row (pd.Series): A row of sensor data with 'ph' and 'turbidity'.
        
        Returns:
            tuple: (is_safe (bool), reason (str))
        """
        ph = row['ph']
        turbidity = row['turbidity']
        
        if pd.isna(ph) or ph == 0:
            return False, "missing pH value"
        if pd.isna(turbidity) or turbidity == 0:
            return False, "missing turbidity value"
        if not (self.ph_min <= ph <= self.ph_max):
            reason = "pH value too high" if ph > self.ph_max else "pH value too low"
            return False, reason
        if turbidity > self.turbidity_max:
            return False, "turbidity too high"
        
        return True, "Safe"
    
    def evaluate_dataframe(self, df):
        """
        Evaluate all rows in the DataFrame for water safety.
        
        Args:
            df (pd.DataFrame): DataFrame with sensor data.
        
        Returns:
            list: List of tuples (sensor_id, location, is_safe, reason).
        """
        results = []
        for _, row in df.iterrows():
            is_safe, reason = self.evaluate_row(row)
            results.append((row['sensor_id'], row['location'], is_safe, reason))
        return results