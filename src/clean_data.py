import pandas as pd
from load_data import load_csv
def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.

    """
# Drop rows with any missing values
    df = df.dropna()

    # Convert timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])  # drop if timestamp conversion failed

    # Ensure numeric columns are non-negative
    numeric_cols = ['pH', 'turbidity', 'dissolved_oxygen', 'temperature']
    for col in numeric_cols:
        df = df[df[col] >= 0]

    #reset index after cleaning
    df = df.reset_index(drop=True)

    return df

