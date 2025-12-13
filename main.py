import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import json

def main():
    print("main")

if __name__ == "__main__":
    main()

# give the option to write path or choose default

target_keywords_df = None
target_keywords_csv_path = Path(
    input("Enter the path to target keywords (must be a .csv): ")
)
if target_keywords_csv_path.suffix == ".csv":
    target_keywords_df = pd.read_csv(target_keywords_csv_path)
else:
    print(f"File type '{target_keywords_csv_path.suffix}' is not a .csv:")

# give the option to write path or choose default

benchmark_keywords_df = None
benchmark_keywords_csv_path = Path(
    input("Enter the path to the keyword list you want to benchmark (must be a .csv): ")
)
if benchmark_keywords_csv_path.suffix == ".csv":
    benchmark_keywords_df = pd.read_csv(benchmark_keywords_csv_path)
else:
    print(f"File type '{benchmark_keywords_csv_path.suffix}' is not a .csv")

# Write default export location to a json file, and add to the .gitignore
