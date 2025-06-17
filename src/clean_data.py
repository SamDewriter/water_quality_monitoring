import pandas as pd
import numpy as np
from sensor import Sensor
def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # remove invalid timestamp
    # Remove duplicates value line
    df = df.drop_duplicates(keep='first')

    # Remove invalid timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])

    temperature_skew = df["temperature"].skew()
    dissolved_oxygen_skew = df["dissolved_oxygen"].skew()

    # replace is based on skew calculation
    if 0 < temperature_skew < 0.5:
        df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
    else:
        df['temperature'] = df['temperature'].fillna(df['temperature'].median())

    if 0 < temperature_skew < 0.5:
        df['dissolved_oxygen'] = df['dissolved_oxygen'].fillna(df['dissolved_oxygen'].mean())
    else:
        df['temperature'] = df['temperature'].fillna(df['temperature'].median())

    return df


def insert_sensor_location(df: pd.DataFrame):

    for sensor_id in np.sort(df['sensor_id'].unique()):
        location = input(f"Enter location for sensor {sensor_id}:")
        df.loc[df['sensor_id'] == sensor_id, 'location'] = str(location)


def count_safe_unsafe_sensor(df: pd.DataFrame):
    sensors = []
    count_safe_sensor = 0
    count_unsafe_sensor = 0

    for sensor_id in np.sort(df['sensor_id'].unique()):
        sensor = Sensor(sensor_id, df[df['sensor_id'] == sensor_id])
        sensors.append(sensor)
        if sensor.is_safe():
            count_safe_sensor = count_safe_sensor + 1
        else:
            count_unsafe_sensor = count_unsafe_sensor + 1
    return count_safe_sensor, count_unsafe_sensor


def save_evaluation_result(df: pd.DataFrame):

    location = []
    status = []
    sensors = []
    ids = []

    for sensor_id in np.sort(df['sensor_id'].unique()):
        sensor = Sensor(sensor_id, df[df['sensor_id'] == sensor_id])
        sensors.append(sensor)

    for sensor in sensors:
        ids.append(sensor.sensor_id)
        location.append(sensor.location)
        status.append(sensor.status)


    result_data = {
        'sensor_id': ids,
        'location': location,
        'status': status
    }

    result_data_df = pd.DataFrame(result_data)
    result_data_df.to_csv('../data/sensor_evaluation_result.csv', index=False)
    return result_data_df
