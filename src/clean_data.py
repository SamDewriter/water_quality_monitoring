import pandas as pd 
def clean_sensor_data(df):
    df['pH'] = pd.to_numeric(df['pH'], errors='coerce')
    df['turbidity'] = pd.to_numeric(df['turbidity'], errors='coerce')
    df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

    df['pH'].fillna(df['pH'].mean(), inplace=True)
    df['turbidity'].fillna(df['turbidity'].mean(), inplace=True)
    df['temperature'].fillna(df['temperature'].mean(), inplace=True)

    df['pH'] = df['pH'].clip(lower=0, upper=14)
    df['turbidity'] = df['turbidity']
    return df
