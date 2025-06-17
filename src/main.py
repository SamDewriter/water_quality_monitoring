import pandas as pd
import os
import sys
from datetime import datetime
from load_data import sensor_data_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

# Import our custom modules
# from load_data import load_csv

def print_results(df):
    """Print results in the expected format."""
    print("\n" + "="*50)
    print("WATER QUALITY ASSESSMENT RESULTS")
    print("="*50)
    
    for _, row in df.iterrows():
        sensor_id = row['sensor_id']
        location = row['location']
        status_emoji = "✅" if row['is_safe'] else "❌"
        status = row['status']
        
        if row['is_safe']:
            print(f"Sensor {sensor_id} at {location}: {status_emoji} {status}")
        else:
            print(f"Sensor {sensor_id} at {location}: {status_emoji} {status} ({row['reason']})")

def save_results_to_csv(df, output_file='results.csv'):
    """Save results to CSV file."""
    # Select relevant columns for output
    output_columns = ['sensor_id', 'location', 'ph', 'turbidity', 'temperature', 
                     'is_safe', 'status', 'reason']
    
    results_df = df[output_columns].copy()
    results_df.to_csv(output_file, index=False)
    print(f"\nResults saved to {output_file}")

def print_summary(df):
    """Print summary statistics."""
    total_sensors = len(df)
    safe_sensors = df['is_safe'].sum()
    unsafe_sensors = total_sensors - safe_sensors
    
    print(f"\n" + "="*30)
    print("SUMMARY")
    print("="*30)
    print(f"Total sensors: {total_sensors}")
    print(f"Safe sensors: {safe_sensors}")
    print(f"Unsafe sensors: {unsafe_sensors}")
    print(f"Safety rate: {(safe_sensors/total_sensors)*100:.1f}%")

def filter_by_location(df, location_filter):
    """Filter data by location."""
    if location_filter:
        filtered_df = df[df['location'].str.contains(location_filter, case=False, na=False)]
        if len(filtered_df) == 0:
            print(f"No sensors found for location: {location_filter}")
            return df
        else:
            print(f"Filtered to {len(filtered_df)} sensors for location: {location_filter}")
            return filtered_df
    return df

def main():
    """Main function to run the water quality monitoring pipeline."""
    print("Water Quality Monitoring System")
    print("="*40)
    
    # Configuration
    data_file = 'clean_sensor_data.csv'
    
    # Check if user wants to filter by location
    location_filter = None
    if len(sys.argv) > 1:
        location_filter = sys.argv[1]
        print(f"Filtering by location: {location_filter}")
    
    try:
        # Step 1: Load data
        print(f"\n1. Loading data from {data_file}...")
        df = sensor_data_csv(data_file)
        
        # Step 2: Clean data
        print("\n2. Cleaning data...")
        cleaned_df = clean_sensor_data(df)
        
        # Step 3: Filter by location if specified
        if location_filter:
            cleaned_df = filter_by_location(cleaned_df, location_filter)
        
        # Step 4: Evaluate water quality
        print("\n3. Evaluating water quality...")
        evaluator = WaterQualityEvaluator()
        results_df = evaluator.evaluate_all_readings(cleaned_df)
        
        # Step 5: Display results
        print_results(results_df)
        
        # Step 6: Print summary
        print_summary(results_df)
        
        # Step 7: Save results (bonus feature)
        save_results_to_csv(results_df)
        
        print(f"\nProcessing completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    # Accept location name from terminal (bonus)
    location = sys.argv[1] if len(sys.argv) > 1 else None
    main(location)

