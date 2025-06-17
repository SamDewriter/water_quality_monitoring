
import pandas as pd

def clean_sensor_data(df):
    df = df.copy()
    sensor_columns = ['pH', 'turbidity', 'temperature']

    # Loop through each sensor column
    for column_name in sensor_columns:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

        # Fill missing values (NaN) with the mean of the column
        df[column_name] = df[column_name].fillna(df[column_name].mean())
    df['pH'] = df['pH'].clip(lower=0, upper=14)

    return df
