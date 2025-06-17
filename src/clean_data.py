import pandas as pd
def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
#handle missing values
numeric_cols =['PH','turbidity','dissolved_oxygen','temperature']
cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].mean())

# Remove impossible values
cleaned_df = cleaned_df[
    (cleaned_df['pH'] > 0) & 
    (cleaned_df['pH'] < 14) & 
    (cleaned_df['turbidity'] >= 0) &
    (cleaned_df['dissolved_oxygen'] >= 0) &
    (cleaned_df['temperature'].between(-20, 60))]

# Remove duplicates
cleaned_df = cleaned_df.drop_duplicates()
return cleaned_df