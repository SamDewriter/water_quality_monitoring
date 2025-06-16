import pandas as pd

# Function to load a CSV file into a Pandas DataFrame
def load_csv(filepath):
    return pd.read_csv(filepath)