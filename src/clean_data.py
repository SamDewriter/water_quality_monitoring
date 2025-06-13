import pandas as pd

def clean_data(df):
    """
    Clean the DataFrame by handling missing values and invalid entries.
    
    Args:
        df (pd.DataFrame): Input DataFrame with sensor data.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Convert pH and turbidity to numeric, coercing errors to NaN
    df_clean['ph'] = pd.to_numeric(df_clean['ph'], errors='coerce')
    df_clean['turbidity'] = pd.to_numeric(df_clean['turbidity'], errors='coerce')
    
    # Handle missing values: fill with mean for pH and turbidity
    df_clean['ph'] = df_clean['ph'].fillna(df_clean['ph'].mean())
    df_clean['turbidity'] = df_clean['turbidity'].fillna(df_clean['turbidity'].mean())
    
    # Ensure temperature is numeric and fill missing with mean
    df_clean['temperature'] = pd.to_numeric(df_clean['temperature'], errors='coerce')
    df_clean['temperature'] = df_clean['temperature'].fillna(df_clean['temperature'].mean())
    
    # Remove invalid entries (e.g., negative pH or turbidity)
    df_clean['ph'] = df_clean['ph'].clip(lower=0, upper=14)  # pH range: 0–14
    df_clean['turbidity'] = df_clean['turbidity'].clip(lower=0)  # Turbidity >= 0
    
    return df_clean
