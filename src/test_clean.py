from load_data import load_data
from clean_data import clean_data

df = load_data("C:/Users/gold/water_quality_monitoring/data/sensor_data.csv")
df_clean = clean_data(df)
print(df_clean)
