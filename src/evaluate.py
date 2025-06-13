import pandas as pd

def evaluate_data(df: pd.DataFrame) -> list:
    """
    Evaluate water quality for each row in the DataFrame.
    
    Args:
        df (pd.DataFrame): Cleaned DataFrame with sensor data (columns: sensor_id, location, ph, turbidity, temperature, [dissolved_oxygen]).
        
    Returns:
        list: List of dictionaries with evaluation results.
    """
    results = []
    for _, row in df.iterrows():
        sensor_id = row['sensor_id']
        location = row['location']
        ph = row['ph']
        turbidity = row['turbidity']
        temperature = row['temperature']
        dissolved_oxygen = row.get('dissolved_oxygen', pd.NA)  # Optional column
        
        reasons = []
        
        # Check for missing values
        if pd.isna(ph):
            reasons.append("missing pH")
        if pd.isna(turbidity):
            reasons.append("missing turbidity")
            
        # Check pH range (6.5–8.5)
        if not pd.isna(ph) and (ph < 6.5 or ph > 8.5):
            reasons.append("pH out of range (6.5-8.5)")
            
        # Check turbidity (<=1.0)
        if not pd.isna(turbidity) and turbidity > 1.0:
            reasons.append("turbidity too high (>1.0)")
            
        # Determine safety
        is_safe = len(reasons) == 0
        reason = ", ".join(reasons) if reasons else ""
        
        # Include dissolved_oxygen in output (optional)
        result = {
            'sensor_id': sensor_id,
            'location': location,
            'ph': ph,
            'turbidity': turbidity,
            'temperature': temperature,
            'is_safe': is_safe,
            'reason': reason
        }
        if not pd.isna(dissolved_oxygen):
            result['dissolved_oxygen'] = dissolved_oxygen
        
        results.append(result)
    
    return results