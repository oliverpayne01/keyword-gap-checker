import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

target_keywords_df = None
target_keywords_csv_path = Path(input("Enter path to target keywords (.csv): "))

if target_keywords_csv_path.suffix == ".csv":
    target_keywords_df = pd.read_csv(target_keywords_csv_path)
else:
    print(f"File type is not a .csv: {target_keywords_csv_path.suffix}")

benchmark_keywords_df = None
benchmark_keywords_csv_path = Path(input("Enter CSV: "))

# Write default export location to a json file, and add to the .gitignore
