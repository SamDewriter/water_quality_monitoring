import pandas as pd
import argparse
from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import evaluate_data

def main(file_path, location_filter=None):
    """
    Run the water quality monitoring pipeline.
    
    Args:
        file_path (str): Path to the input CSV file.
        location_filter (str, optional): Filter results by location name.
    """
    # Load data
    df = load_csv(file_path)
    if df is None:
        return
    
    # Clean data
    df_clean = clean_sensor_data(df)
    
    # Filter by location if provided
    if location_filter:
        df_clean = df_clean[df_clean['location'].str.lower() == location_filter.lower()]
        if df_clean.empty:
            print(f"No data found for location: {location_filter}")
            return
    
    # Evaluate water safety
    results = evaluate_data(df_clean)
    
    # Count safe vs unsafe lakes
    safe_count = sum(1 for r in results if r['is_safe'])
    unsafe_count = len(results) - safe_count
    
    # Print results
    print("\n=== Water Quality Analysis Results ===")
    for result in results:
        status = "✅ Safe" if result['is_safe'] else f"❌ Unsafe ({result['reason']})"
        print(f"Sensor {result['sensor_id']} at {result['location']}: {status}")
    
    # Print summary
    print(f"\nSummary: {safe_count} safe lakes, {unsafe_count} unsafe lakes")
    
    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('data/results.csv', index=False)
    print("Results saved to data/results.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Water Quality Monitoring Pipeline")
    parser.add_argument('--file', default='data/sensor_data.csv', help='Path to input CSV file')
    parser.add_argument('--location', help='Filter by location name')
    args = parser.parse_args()
    
    main(args.file, args.location)