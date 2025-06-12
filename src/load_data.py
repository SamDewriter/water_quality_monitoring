# src/load_data.py
import pandas as pd

def load_sensor_data(file_path):
    """
    Loading sensor data from a CSV file into a pandas DataFrame.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded sensor data.
    Raises:
        FileNotFoundError: If the CSV file is not found.
    """

    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} is not found.")
        raise