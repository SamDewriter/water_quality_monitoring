import csv
from typing import List, Dict

def load_csv_file(file_path: str) -> List[Dict]:
    """
    Load data from a CSV file into a list of dictionaries.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        List of dictionaries representing each row of data
    """
    data = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return []