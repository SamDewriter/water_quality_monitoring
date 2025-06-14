import pandas as pd

# Function to clean sensor data by converting 'pH' and 'turbidity' columns to numeric values.
def clean_sensor_data(df):
    df = df.copy()
    
    # Convert to numeric, coercing invalid values to NaN
    df['pH'] = pd.to_numeric(df['pH'], errors='coerce')
    df['turbidity'] = pd.to_numeric(df['turbidity'], errors='coerce')
    df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
    
    return df

# Function to assign unique sensor IDs and lake locations to each row in the dataset.
def assign_sensor_and_location(df):
    df = df.copy()
    df['sensor'] = [f"Sensor {str(i+1).zfill(3)}" for i in range(len(df))]
    df['location'] = [f"Lake {chr(65 + i)}" for i in range(len(df))]
    return df