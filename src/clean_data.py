# src/clean_data.py
import pandas as pd

def clean_sensor_data(df):
        # Create a copy to avoid modifying the original DF
    df_clean = df.copy()
    
    df_clean['ph'] = df_clean['ph'].fillna(0)  
    df_clean['turbidity'] = df_clean['turbidity'].fillna(0)
    
    # Ensure numeric columns are of the correct type
    df_clean['ph'] = pd.to_numeric(df_clean['ph'], errors='coerce').fillna(0)
    df_clean['turbidity'] = pd.to_numeric(df_clean['turbidity'], errors='coerce').fillna(0)
    df_clean['temperature'] = pd.to_numeric(df_clean['temperature'], errors='coerce').fillna(0)
    
    return df_clean