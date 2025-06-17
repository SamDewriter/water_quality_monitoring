import pandas as pd
def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    if df is None:
        print("Cannot perform data cleaning. Kindly provide raw data frame")
    
    print(df.info()) # inspecting the data for anonormallies 
    print(df.isnull().sum()) # This will show a count of missing values for each column

    # create a copy of the data
    df_copy = df.copy()
    # ensure columns should have numeric values:
    numeric_columns = ["ph", "turbidity", "dissolved_oxygen", "temperature"]

    for column in numeric_columns:
        if column in df_copy.columns:
            df_copy[column] = pd.to_numeric(df_copy[column], errors="coerce") # convert to numeric values
            df_copy[column] = df_copy[column].round(3) #convert to three decimal places
    
    return df_copy


