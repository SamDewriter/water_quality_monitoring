import pandas as pd
import csv

def load_csv(filepath: str = 'data/sensor_data.csv') -> pd.DataFrame:
    """
    Load water quality sensor data from a CSV file.
    
    Args:
        filepath: Path to the CSV file (default: 'data/sensor_data.csv')
        
    Returns:
        pd.DataFrame: Loaded sensor data or empty DataFrame if loading fails
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded data from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return pd.DataFrame()
