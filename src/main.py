from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator  

# Load and clean
file_path = r"C:\Users\USER\Desktop\codebook\alt_class\water_quality_monitoring\data\sensor_data.csv"
raw_df = load_csv(file_path)
print(raw_df.columns)
df_cleaned = clean_sensor_data(raw_df)

# Evaluate
evaluator = WaterQualityEvaluator(ph_range=(6.5, 8.5), turbidity_threshold=1.0)
evaluated_df = evaluator.evaluate(df_cleaned)

# Save
evaluated_df.to_csv("processed_data.csv", index=False)
print("✅ Water quality evaluation complete and saved to 'processed_data.csv'.")
