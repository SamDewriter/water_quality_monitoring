from load_data import load_csv
from clean_data import clean_sensor_data, insert_sensor_location, count_safe_unsafe_sensor, save_evaluation_result

#load
df = load_csv("../data/sensor_data.csv")

#clean
df = clean_sensor_data(df)

# insert the location of sensor
insert_sensor_location(df)

# save cleaned data
df.to_csv('../data/sensor_data_clean.csv', index=False)

#load clean data
df = load_csv("../data/sensor_data_clean.csv")

# evaluition results
result_data_df = save_evaluation_result(df)
count_safe_sensor, count_unsafe_sensor = count_safe_unsafe_sensor(df)

print("\n", result_data_df)
print(f"\nFound {count_safe_sensor} sensors Safe")
print(f"Found {count_unsafe_sensor} sensors Unsafe")