# Import necessary functions from custom modules
from load_data import load_csv
from clean_data import clean_sensor_data, assign_sensor_and_location
from evaluate import evaluate_and_save_results


# Main Execution: Load, Clean, Label, and Filter Water Quality Data
if __name__ == "__main__":
    df_raw = load_csv("/Users/eserogheneoghojafor/water_quality_monitoring/data/sensor_data.csv")
    df_clean = clean_sensor_data(df_raw)
    df_with_labels = assign_sensor_and_location(df_clean)

    lake_choice = input("Enter the lake you want to evaluate (e.g. 'Lake A'), or press Enter to evaluate all lakes: ").strip()

    if lake_choice:
        df_selected = df_with_labels[df_with_labels['location'] == lake_choice]
        if df_selected.empty:
            print(f"No data found for '{lake_choice}'. Exiting.")
            exit()
    else:
        df_selected = df_with_labels

    output_path = "/Users/eserogheneoghojafor/water_quality_monitoring/results/results.csv"

    evaluate_and_save_results(df_selected, output_path, show_top_n=5)