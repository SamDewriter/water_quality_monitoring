from load_data import load_csv_file
from clean_data import clean_data
from evaluate import WaterQualityEvaluator

def main():
    # File paths
    input_file = r"C:\Users\HP\Water_Quality_Monitoring\water_quality_monitoring\data\sensor_data.csv"
    
    # Load data
    raw_data = load_csv_file(input_file)
    if not raw_data:
        print("No data loaded. Exiting.")
        return
    
    # Clean data
    cleaned_data = clean_data(raw_data)
    
    # Evaluate data
    evaluator = WaterQualityEvaluator()
    results = []
    
    for sensor in cleaned_data:
        evaluation = evaluator.evaluate_sensor(sensor)
        results.append(evaluator.format_result(evaluation))
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()