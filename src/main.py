import os
import pandas as pd
from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator


def main():
    # Step 1: Load data
    data_path = os.path.join("..", "data", "sensor_data.csv")
    df = load_csv(data_path)

    if df.empty:
        print("No data to process.")
        return

    # Step 2: Clean data
    cleaned_df = clean_sensor_data(df)


    # Step 3: Evaluate data
    evaluator = WaterQualityEvaluator()
    results = []

    for _, row in cleaned_df.iterrows():  # use original df to preserve missing entries
        status = evaluator.get_reason(row)
        print(f"Sensor {row['sensor_id']} at {row['location']}: {status}")
        results.append({
            "sensor_id": row["sensor_id"],
            "location": row["location"],
            "status": status
        })

    # Step 4 (Bonus): Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv("results.csv", index=False)

    # Step 5 (Bonus): Summary counts
    safe_count = results_df["status"].str.contains("✅").sum()
    unsafe_count = results_df.shape[0] - safe_count
    print(f"Sensor {row['sensor_id']} at {row['location']}: {status}")
    

if __name__ == "__main__":
    main()
