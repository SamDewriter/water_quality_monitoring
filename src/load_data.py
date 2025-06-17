import pandas as pd
from clean_data import clean_sensor_data
import os


def sensor_data_csv(filepath: str) -> pd.DataFrame:

    """
    Load sensor data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    import pandas as pd

    try:
        data = pd.load_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"No data in file: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return pd.DataFrame()

