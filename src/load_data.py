import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    df = df.copy()
    df = df.dropna(subset=["pH", "turbidity"])
    df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
    df["dissolved_oxygen"] = df["dissolved_oxygen"].fillna(df["dissolved_oxygen"].mean())
    return df
