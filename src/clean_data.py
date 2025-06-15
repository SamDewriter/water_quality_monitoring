def clean_data(df):
    df = df.copy()
    df = df.dropna(subset=["pH", "turbidity"])
    df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
    df["dissolved_oxygen"] = df["dissolved_oxygen"].fillna(df["dissolved_oxygen"].mean())
    return df
