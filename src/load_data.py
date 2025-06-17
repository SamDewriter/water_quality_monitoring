import pandas as pd

def read_csv(filepath: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(filepath)
        print("File loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file is corrupted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df.drop_duplicates()
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])

    df = df.reset_index(drop=True)
    print("Data cleaned successfully.")
    return df




