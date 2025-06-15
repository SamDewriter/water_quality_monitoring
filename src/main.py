from load_data import load_data
from clean_data import clean_data
from evaluate import WaterQualityEvaluator

def main():
    file_path = "C:/Users/Administrator/Desktop/water_quality_monitoring/data/sensor_data.csv"  
    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        evaluator = WaterQualityEvaluator()
        results = evaluator.evaluate(df)
        results.to_csv("evaluated_results.csv", index=False)
        print(results[['sensor_id', 'pH', 'turbidity', 'is_safe']].head(10))
        print("✅ Results saved to evaluated_results.csv")
    else:
        print("❌ Failed to load the dataset.")

if __name__ == "__main__":
    main()

