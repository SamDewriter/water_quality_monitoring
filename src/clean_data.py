import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Normalize column names
    df.columns = df.columns.str.lower()

    # Convert pH and turbidity to numeric values, coercing errors
    df['ph'] = pd.to_numeric(df['ph'], errors='coerce')
    df['turbidity'] = pd.to_numeric(df['turbidity'], errors='coerce')

    # Drop rows with missing pH or turbidity values
    df = df.dropna(subset=['ph', 'turbidity'])

    # Map sensor_id to location
    lake_map = {
        'SENSOR_001': 'Lake A',
        'SENSOR_002': 'Lake B',
        'SENSOR_003': 'Lake C',
        'SENSOR_004': 'Lake D',
        'SENSOR_005': 'Lake E',
        'SENSOR_006': 'Lake F',
        'SENSOR_007': 'Lake G',
        'SENSOR_008': 'Lake H',
        'SENSOR_009': 'Lake I',
        'SENSOR_010': 'Lake J',
        'SENSOR_011': 'Lake K',
        'SENSOR_012': 'Lake L',
        'SENSOR_013': 'Lake M',
        'SENSOR_014': 'Lake N',
        'SENSOR_015': 'Lake O',
        'SENSOR_016': 'Lake P',
        'SENSOR_017': 'Lake Q',
        'SENSOR_018': 'Lake R',
        'SENSOR_019': 'Lake S',
        'SENSOR_020': 'Lake T'
    }

    df['location'] = df['sensor_id'].map(lake_map)

    return df
