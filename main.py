import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import json


def get_config():
    config_path = "./config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as json_file:
            return json.load(json_file)
    else:
        return None


config = get_config()

# function to save
# function to allow save


def get_target_keywords():
    # If we have a saved path, use that, otherwise input path and give option to save

    if config["target_keywords_path"]:
        
    else:
        target_keywords_path = Path(input("Enter the path to target keywords (must be a .csv): "))


# def analyze_gap(target_keywords_df, benchmark_keywords_df):
#     # logic
#     return


def main():
    target_keywords_df = get_target_keywords()
    #
    # analyze_gap(get_target_keywords())


if __name__ == "__main__":
    main()
