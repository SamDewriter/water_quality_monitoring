import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load sensor data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded data from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return pd.DataFrame() # Return empty DataFrame on error
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return pd.DataFrame()
