import pandas as pd
import os

def extract_data():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '..', 'data', 'IPL.csv')
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully!")
        print(f"Total rows: {len(df)}")
        print(f"Total columns: {len(df.columns)}")
        print(f"\nColumn names:")
        print(df.columns.tolist())
        print(f"\nFirst 3 rows:")
        print(df.head(3))
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    df = extract_data()
