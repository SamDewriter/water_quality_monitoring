from typing import List, Dict

def clean_data(data: List[Dict]) -> List[Dict]:
    """
    Clean the sensor data by handling missing values and converting types.
    
    Args:
        data: List of dictionaries containing raw sensor data
        
    Returns:
        List of dictionaries with cleaned data
    """
    cleaned_data = []
    
    for row in data:
        cleaned_row = row.copy()
        
        # Convert numeric fields to float if they exist, else None
        for field in ['ph', 'turbidity', 'temperature']:
            if field in cleaned_row and cleaned_row[field]:
                try:
                    cleaned_row[field] = float(cleaned_row[field])
                except ValueError:
                    cleaned_row[field] = None
            else:
                cleaned_row[field] = None
                
        cleaned_data.append(cleaned_row)
    
    return cleaned_data
