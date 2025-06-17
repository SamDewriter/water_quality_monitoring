# main.py
import pandas as pd
from load_data import read_csv, clean_data
from evaluate import WaterQualityEvaluator
from sensor import SensorReading
import csv

def run_pipeline(filepath: str):
    location_input = input("Enter the lake or location name to analyze: ").strip()

    df = read_csv(filepath)
    if df is None:
        print("Failed to load data.")
        return

    df = clean_data(df)

    evaluator = WaterQualityEvaluator(ph_min=6.5, ph_max=8.5, turbidity_max=5.0)
    results = []

    for _, row in df.iterrows():
        sensor = SensorReading(
            sensor_id=row.get('sensor_id', 'Unknown'),
            location=row.get('location', 'Unknown location'),
            ph=row.get('ph'),
            turbidity=row.get('turbidity')
        )

        evaluated = evaluator.evaluate(sensor)

        # Filter by location name if provided
        if location_input.lower() in evaluated.location.lower():
            print(f"{evaluated.sensor_id} at {evaluated.location}: {evaluated.safety_status}")

        results.append(evaluated)

    # Save results to CSV
    with open("results.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["sensor_id", "location", "ph", "turbidity", "safety_status"])
        writer.writeheader()
        for sensor in results:
            writer.writerow(sensor.to_dict())

    # Count safe/unsafe by location
    safe = sum(1 for s in results if s.safety_status == "Safe")
    unsafe = len(results) - safe
    print(f"\nSummary: {safe} safe readings, {unsafe} unsafe readings.")

if __name__ == "__main__":
    run_pipeline(r"C:\Users\user\water_quality_monitoring\water_quality_monitoring\data\sensor_data.csv")



