from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator
import pandas as pd

def show_menu():
    print("\n🌊 Water Quality Monitoring Menu")
    print("1. Load and view raw sensor data")
    print("2. Clean data (handle missing/invalid)")
    print("3. Evaluate water safety and save results")
    print("4. Exit")

# Session variables
raw_df = None
cleaned_df = None
results_df = None
data_path = None

while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        data_path = input(" Enter full path to the sensor data CSV file: ").strip()
        try:
            raw_df = load_csv(data_path)
            print("\n Raw Sensor Data Preview:")
            print(raw_df.head())
        except FileNotFoundError:
            print("❌ File not found. Please check the path and try again.")

    elif choice == "2":
        if raw_df is None:
            print("⚠️ Please load the raw data first (Option 1).")
        else:
            cleaned_df = clean_sensor_data(raw_df)
            print("\n✅ Cleaned Data Preview:")
            print(cleaned_df.head())

    elif choice == "3":
        if cleaned_df is None:
            print(" Please clean the data first (Option 2).")
        else:
            location = input("📍 Enter the location name for this data (e.g., 'Lake A'): ").strip()
            cleaned_df["location"] = location  # Add location to the DataFrame

            evaluator = WaterQualityEvaluator()
            results_df = evaluator.evaluate(cleaned_df)

            print("\n📋 Evaluation Results:")
            for _, row in results_df.iterrows():
                print(f"{row['sensor']}: {row['status']}")

            # Save to CSV
            save_path = "results.csv" if not data_path else data_path.replace(".csv", "_results.csv")
            results_df.to_csv(save_path, index=False)
            print(f"💾 Results saved to {save_path}")



    elif choice == "4":
        print("👋 Exiting. Stay hydrated!")
        break

    else:
        print("❌ Invalid choice. Please enter a number between 1 and 4.")
