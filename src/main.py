import sys
import pandas as pd
from load_data import load_data
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

def assign_sensor_and_location(df):
    df = df.copy()
    df['sensor_id'] = [f"Sensor {i+1:03d}" for i in range(len(df))]
    df['location'] = [f"Lake {chr(65 + (i % 26))}" for i in range(len(df))]
    return df

def main(location_filter=None):
    try:
        df = load_data(r"C:\Users\LFT\Documents\water_quality_monitoring\data\sensor_data.csv")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except pd.errors.EmptyDataError as e:
        print(f"Error: CSV file is empty - {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    df = assign_sensor_and_location(df)
    df_clean = clean_sensor_data(df)

    evaluator = WaterQualityEvaluator()
    for _, row in df_clean.iterrows():
        evaluator.add_reading(
            row['sensor_id'],
            row['location'],
            row['pH'],
            row['turbidity'],
            row['temperature']
        )

    results = evaluator.evaluate_all()

    if location_filter:
        results = [(sid, loc, safe, reason) for sid, loc, safe, reason in results
                   if location_filter.lower() in loc.lower()]

    for sensor_id, location, is_safe, reason in results:
        status = "[Safe]" if is_safe else f"[Unsafe] ({reason})"
        print(f"Sensor {sensor_id} at {location}: {status}")

    safe_count, unsafe_count = evaluator.count_safety_status()
    print(f"\nSummary: {safe_count} safe, {unsafe_count} unsafe")

    results_df = pd.DataFrame(
        results,
        columns=['sensor_id', 'location', 'is_safe', 'reason']
    )
    results_df.to_csv(r"C:\Users\LFT\Documents\water_quality_monitoring\data\results.csv", index=False)
    print("Results saved to data/results.csv")

if __name__ == "__main__":
    location = sys.argv[1] if len(sys.argv) > 1 else None
    main(location)