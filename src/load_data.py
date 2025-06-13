import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame or None if loading fails.
    """
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        print(f"Successfully loaded {file_path} with {len(df)} rows.")
        print(f"Columns: {list(df.columns)}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None