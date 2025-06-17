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
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print(f"Error: Failed to parse CSV file at {filepath}")
        return pd.DataFrame()
