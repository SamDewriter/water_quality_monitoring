from load_data import load_data
from clean_data import clean_data
from evaluate import WaterQualityEvaluator

df = load_data("../data/sensor_data.csv")
df_clean = clean_data(df)

evaluator = WaterQualityEvaluator()
for _, row in df_clean.iterrows():
    evaluator.add_reading(
        row['sensor_id'],
        row['location'],
        row['ph'],
        row['turbidity'],
        row['temperature']
    )

results = evaluator.evaluate_all()
for sensor_id, location, is_safe, reason in results:
    status = "Safe" if is_safe else f"Unsafe ({reason})"
    print(f"Sensor {sensor_id} at {location}: {status}")