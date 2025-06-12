# src/main.py
import argparse, pandas as pd

from load_data import load_sensor_data
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

def main(file_path, location_filter=None):
    """
    Run the water quality monitoring pipeline.
    
    Args:
        file_path (str): Path to the sensor data CSV file.
        location_filter (str, optional): Filter data by location name.
    """
    # Load data
    df = load_sensor_data(file_path)
    
    # Clean data
    df_clean = clean_sensor_data(df)
    
    # Filter by location if provided
    if location_filter:
        df_clean = df_clean[df_clean['location'].str.contains(location_filter, case=False, na=False)]
        if df_clean.empty:
            print(f"No data found for location: {location_filter}")
            return
    
    # Evaluate water quality
    evaluator = WaterQualityEvaluator()
    results = evaluator.evaluate_dataframe(df_clean)
    
        
    # Print results
    for sensor_id, location, is_safe, reason in results:
        status = "✅ Safe" if is_safe else f"❌ Unsafe ({reason})"
        print(f"Sensor {sensor_id} at {location}: {status}")
    
       
    # Save results to CSV
    results_df = pd.DataFrame(
        results, columns=['sensor_id', 'location', 'is_safe', 'reason'])

    results_df.to_csv('results.csv', index=False)
    print("Results saved to results.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Water Quality Monitoring Pipeline")
    parser.add_argument('--file', default='data/sensor_data.csv', help='Path to sensor data CSV')
    parser.add_argument('--location', help='Filter by location name')
    args = parser.parse_args()
    
    main(args.file, args.location)