import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Args:
        df (pd.DataFrame): Input DataFrame with sensor data (columns: sensor_id, timestamp, pH, turbidity, dissolved_oxygen, temperature).

    Returns:
        pd.DataFrame: Cleaned DataFrame with missing or invalid values handled.

    Raises:
        KeyError: If required columns are missing from the DataFrame.
    """
    # Create a copy to avoid modifying the original DataFrame
    df_clean = df.copy()
    
    # Define expected columns (based on your CSV)
    expected_columns = ['sensor_id', 'timestamp', 'pH', 'turbidity', 'temperature']  # Excluding dissolved_oxygen if not used
    required_columns = ['sensor_id', 'pH', 'turbidity', 'temperature']  # Minimum required for analysis
    
    # Check for missing required columns
    missing_columns = [col for col in required_columns if col not in df_clean.columns]
    if missing_columns:
        raise KeyError(f"Missing required columns in CSV: {missing_columns}. Found columns: {list(df_clean.columns)}")
    
    # Rename columns to match expected names (e.g., pH -> ph)
    df_clean = df_clean.rename(columns={
        'pH': 'ph',
        'timestamp': 'location'  # Treat timestamp as location for compatibility
    })
    
    # Ensure numeric columns are of correct type
    df_clean['ph'] = pd.to_numeric(df_clean['ph'], errors='coerce')
    df_clean['turbidity'] = pd.to_numeric(df_clean['turbidity'], errors='coerce')
    df_clean['temperature'] = pd.to_numeric(df_clean['temperature'], errors='coerce')
    if 'dissolved_oxygen' in df_clean.columns:
        df_clean['dissolved_oxygen'] = pd.to_numeric(df_clean['dissolved_oxygen'], errors='coerce')
    
    # Handle missing values by replacing with pd.NA
    df_clean['ph'] = df_clean['ph'].fillna(pd.NA)
    df_clean['turbidity'] = df_clean['turbidity'].fillna(pd.NA)
    if 'dissolved_oxygen' in df_clean.columns:
        df_clean['dissolved_oxygen'] = df_clean['dissolved_oxygen'].fillna(pd.NA)
    
    # Handle invalid entries
    # pH: Must be between 0 and 14; otherwise, set to pd.NA
    df_clean['ph'] = df_clean['ph'].apply(lambda x: x if pd.notna(x) and 0 <= x <= 14 else pd.NA)
    # Turbidity: Must be non-negative; otherwise, set to pd.NA
    df_clean['turbidity'] = df_clean['turbidity'].apply(lambda x: x if pd.notna(x) and x >= 0 else pd.NA)
    
    # Drop rows where sensor_id is missing
    df_clean = df_clean.dropna(subset=['sensor_id'])
    
    # If location is missing, add a placeholder (since timestamp is used as location)
    if 'location' not in df_clean.columns:
        df_clean['location'] = 'Unknown Location'
    
    print(f"Cleaned data: {len(df_clean)} rows remaining.")
    return df_clean