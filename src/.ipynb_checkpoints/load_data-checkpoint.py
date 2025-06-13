import pandas as pd

def load_data("C:/Users/DKINUSH/Desktop/water_quality_monitoring/data/sensor_data.csv"):
    ""
    Load CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
    
    Raises:
        FileNotFoundError: If the file doesnt exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path} with {len(df)} rows.")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        raise
    except pd.errors.EmptyDataError:
        print(f"Error: File {file_path} is empty.")
        raise"""
