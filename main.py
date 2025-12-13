import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import json

config = None


def get_config():
    config_path = "./config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as json_file:
            return json.load(json_file)
    else:
        new_config = {"target_keywords_path": "/test_path"}
        with open(config_path, "w") as json_file:
            json.dump(new_config, json_file)
        return new_config


target_keywords_df = None


def get_target_keywords():
    config_path = Path("./config.json")
    if config_path:
        print(config_path)
        # give the option to write a new path or use the default
    else:
        target_keywords_csv_path = Path(
            input("Enter the path to target keywords (must be a .csv): ")
        )
        print("config path does not exist")

    if target_keywords_csv_path.suffix == ".csv":
        target_keywords_df = pd.read_csv(target_keywords_csv_path)
    else:
        print(f"File type '{target_keywords_csv_path.suffix}' is not a .csv:")


# benchmark_keywords_df = None
# benchmark_keywords_csv_path = Path(
#     input("Enter the path to the keyword list you want to benchmark (must be a .csv): ")
# )
# if benchmark_keywords_csv_path.suffix == ".csv":
#     benchmark_keywords_df = pd.read_csv(benchmark_keywords_csv_path)
# else:
#     print(f"File type '{benchmark_keywords_csv_path.suffix}' is not a .csv")

# Write default export location to a json file, and add to the .gitignore


def main():
    global config
    config = get_config()
    print(config)
    # get_target_keywords()


if __name__ == "__main__":
    main()
