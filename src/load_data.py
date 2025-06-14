import pandas as pd 

filepath = r"C:\Users\USER\Desktop\codebook\alt_class\water_quality_monitoring\data\sensor_data.csv" 

def load_csv(filepath: str) -> pd.DataFrame:
    # Load the CSV file and parse the timestamp column as datetime
    df = pd.read_csv(filepath, parse_dates=["timestamp"])
    return df
