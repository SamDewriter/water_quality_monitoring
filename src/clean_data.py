import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """

    print("Cleaning sensor data...")
    # drop rows with any missing ph or turbidity values
    df = df.dropna(subset=['pH', 'turbidity'])


    print("Data cleaning complete.")
    return df.reset_index(drop=True)  # Reset index after dropping rows