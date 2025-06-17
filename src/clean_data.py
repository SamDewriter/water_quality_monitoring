import numpy as np
import pandas as pd


def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Create a copy to avoid modifying original data

    cleaned_df = df.copy()
    
    # Add flags for missing data
    cleaned_df['missing_ph'] = cleaned_df['ph'].isna()
    cleaned_df['missing_turbidity'] = cleaned_df['turbidity'].isna()
    cleaned_df['missing_temperature'] = cleaned_df['temperature'].isna()
    
    # Handle invalid pH values (should be between 0-14)
    invalid_ph_mask = (cleaned_df['ph'] < 0) | (cleaned_df['ph'] > 14)
    cleaned_df.loc[invalid_ph_mask, 'ph'] = np.nan
    cleaned_df.loc[invalid_ph_mask, 'missing_ph'] = True
    
    # Handle invalid turbidity values (should be non-negative)
    invalid_turbidity_mask = cleaned_df['turbidity'] < 0
    cleaned_df.loc[invalid_turbidity_mask, 'turbidity'] = np.nan
    cleaned_df.loc[invalid_turbidity_mask, 'missing_turbidity'] = True
    
    # Handle invalid temperature values (reasonable range: -10 to 50°C)
    invalid_temp_mask = (cleaned_df['temperature'] < -10) | (cleaned_df['temperature'] > 50)
    cleaned_df.loc[invalid_temp_mask, 'temperature'] = np.nan
    cleaned_df.loc[invalid_temp_mask, 'missing_temperature'] = True
    
    # Fill missing sensor_id if needed
    if cleaned_df['sensor_id'].isna().any():
        cleaned_df['sensor_id'] = cleaned_df['sensor_id'].fillna('Unknown')
    
    # Fill missing location if needed
    if cleaned_df['location'].isna().any():
        cleaned_df['location'] = cleaned_df['location'].fillna('Unknown Location')
    
    print(f"Data cleaning completed. Found {cleaned_df['missing_ph'].sum()} missing pH values, "
          f"{cleaned_df['missing_turbidity'].sum()} missing turbidity values, "
          f"{cleaned_df['missing_temperature'].sum()} missing temperature values.")
    
    return cleaned_df

