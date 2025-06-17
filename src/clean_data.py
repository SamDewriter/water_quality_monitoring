import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # drop rows with missing values
    df = df.dropna()
    
    # drop duplicate rows
    df = df.drop_duplicates()
    
    # standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    # convert date column to datetime type
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])  # remove rows where date conversion failed
    
    # reset index
    df = df.reset_index(drop=True)

    print("Data cleaned successfully.")
    return df

