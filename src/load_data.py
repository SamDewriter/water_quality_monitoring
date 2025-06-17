import pandas as pd


def load_csv(filepath: str):
    """
    Load sensor data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return(df)


