import pandas as pd
from load_data import load_csv  
import numpy as np

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    # Convert to numeric, set invalids to NaN
    df["pH"] = pd.to_numeric(df["pH"], errors="coerce")
    df["turbidity"] = pd.to_numeric(df["turbidity"], errors="coerce")

    # Replace invalid values with NaN
    df.loc[(df["pH"] <= 0) | (df["pH"] > 14), "pH"] = np.nan
    df.loc[df["turbidity"] < 0, "turbidity"] = np.nan

    # Drop rows with NaNs in critical columns
    initial_len = len(df)
    df.dropna(subset=["pH", "turbidity"], inplace=True)
    cleaned_len = len(df)

    print(f"✅ Cleaned sensor data: {initial_len - cleaned_len} invalid rows removed.")

    return df


