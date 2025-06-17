import sys
import pandas as pd
from pathlib import Path
from load_data import load_data
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

DATA_PATH = Path(r"C:\Users\donald.chuku\water_quality_monitoring\data")

def assign_sensor_and_location(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns sensor IDs and locations to the dataframe.
    Sensor ID: Sensor 001, Sensor 002, ...
    Location: Lake A, Lake B, ...
    """
    df = df.copy()
    df['sensor_id'] = [f"Sensor {i+1:03d}" for i in range(len(df))]
    df['location'] = [f"Lake {chr(65 + (i % 26))}" for i in range(len(df))]
    return df

def main(location_filter: str = None):
    try:
        df = load_data(DATA_PATH / "sensor_data.csv")
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
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

    # Apply optional location filtering
    if location_filter:
        location_filter = location_filter.lower()
        results = [r for r in results if location_filter in r[1].lower()]

    # Display each result
    for sensor_id, location, is_safe, reason in results:
        status = "[Safe]" if is_safe else f"[Unsafe] ({reason})"
        print(f"{sensor_id} at {location}: {status}")

    print(f"\nShowing first {min(10, len(results))} of {len(results)} results:\n")
    for sensor_id, location, is_safe, reason in results[:10]:
        status = "[Safe]" if is_safe else f"[Unsafe] ({reason})"
        print(f"{sensor_id} at {location}: {status}")
        
    # Summary
    safe_count, unsafe_count = evaluator.count_safety_status()
    print(f"\nSummary: {safe_count} safe, {unsafe_count} unsafe")

    # Save results
    results_df = pd.DataFrame(results, columns=['sensor_id', 'location', 'is_safe', 'reason'])
    output_file = DATA_PATH / "results.csv"
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Allow optional location filtering from command-line
    location = sys.argv[1] if len(sys.argv) > 1 else None
    main(location)
