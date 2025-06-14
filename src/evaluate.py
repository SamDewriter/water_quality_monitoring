# Importing necessary module
import pandas as pd
import os
import csv

# Class for evaluating water quality based on pH and turbidity thresholds
class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, pH, turbidity): 
        if pd.isna(pH):
            return (False, "missing pH")
        if pd.isna(turbidity):
            return (False, "missing turbidity")
        if pH < self.ph_range[0]:
            return (False, "pH too low")
        if pH > self.ph_range[1]:
            return (False, "pH too high")
        if turbidity > self.turbidity_threshold:
            return (False, "turbidity too high")

        return (True, "Safe")

# Evaluates each sensor's data and saves the results to a CSV file
def evaluate_and_save_results(df, output_path, show_top_n=5):
    evaluator = WaterQualityEvaluator()
    results = []
    safe_count = 0
    unsafe_count = 0

    print("\n🔎 Evaluation Summary:\n")

    # Evaluate all sensor readings
    for idx, row in df.iterrows():
        sensor = row['sensor']
        sensor_id = int(sensor.split()[-1])
        location = row['location']
        pH = row.get('pH')
        turbidity = row.get('turbidity')
        temperature = row.get('temperature', '')

        is_safe, reason = evaluator.is_safe(pH, turbidity)
        status = "✅ Safe" if is_safe else f"❌ Unsafe ({reason})"

        if is_safe:
            safe_count += 1
        else:
            unsafe_count += 1

        results.append({
            "sensor": sensor,  # needed just for preview
            "status": status,  # needed just for preview
            "sensor_id": sensor_id,
            "location": location,
            "ph": pH,
            "turbidity": turbidity,
            "temperature": temperature,
        })

    # Printing evaluation summary
    print(f"Total Sensors Evaluated: {len(results)}")
    print(f"✅ Safe Sensors: {safe_count}")
    print(f"❌ Unsafe Sensors: {unsafe_count}\n")

    # Printing top N results as a preview
    print(f" Preview of Top {show_top_n} Results:\n")
    for entry in results[:show_top_n]:
        print(f"{entry['sensor']} at {entry['location']}: {entry['status']}")

    #Saving only the top N results to CSV (without preview fields)
    export_results = [
        {
            "sensor_id": r["sensor_id"],
            "location": r["location"],
            "ph": r["ph"],
            "turbidity": r["turbidity"],
            "temperature": r["temperature"],
        }
        for r in results[:show_top_n]
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["sensor_id", "location", "ph", "turbidity", "temperature"])
        writer.writeheader()
        writer.writerows(export_results)

    print(f"\nTop {show_top_n} results saved to '{output_path}'")