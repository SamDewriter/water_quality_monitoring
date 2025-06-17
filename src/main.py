from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator
import pandas as pd

def main():

    print("Starting Water Quality Monitoring Pipeline...")
    # Load data
    data = load_csv('data/sensor_data.csv')
    
    # Clean data
    cleaned_data = clean_sensor_data(data)
    # Evaluate water quality
    evaluator = WaterQualityEvaluator()

    print("\n--- Water Quality Evaluation Results ---")

    results = []
    for index, row in data.iterrows():
        location = f"Sensor {index + 1} at Lake {index + 1}"
        is_safe, reasons = evaluator.is_safe(row)
        if is_safe:
            print(f"{location}: ✅ Safe")
            results.append({"Location": location, "Status": "Safe", "Reason": ""})
        else:
            reason_str = ", ".join(reasons)
            print(f"{location}: ❌ Unsafe ({reason_str})")
            results.append({"Location": location, "Status": "Unsafe", "Reason": reason_str})

    pd.DataFrame(results).to_csv('data/evaluation_results.csv', index=False)
    print("\nEvaluation results saved to 'data/evaluation_results.csv'.")

if __name__ == "__main__":
    main()


