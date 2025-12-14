import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import json


def create_config():
    with open("./config.json", "w") as json_file:
        json.dump({}, json_file)


def set_config(key, value):
    None


def get_config():
    config_path = "./config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as json_file:
            return json.load(json_file)
    else:
        return None


config = get_config()


def allow_save(key, value):
    # display a Y / N save input
    allow_save_input = Path(
        input("Save selected target keywords path as default? (Y / N): ").upper()
    )
    if allow_save_input == "Y":
        if config == None:
            create_config()
        set_config(key, value)


def get_target_keywords():
    if config == None or not config["target_keywords_path"]:
        target_keywords_path = Path(
            input(
                "Enter the path to target keywords (must be a .csv): "
            )  # we might be able to consolidate this
        )
        while not os.path.exists(target_keywords_path):
            print(target_keywords_path)
            target_keywords_path = Path(
                input("Enter the path to target keywords (must be a .csv): ")
            )

            if os.path.exists(target_keywords_path):
                if target_keywords_path.suffix == ".csv":
                    allow_save("target_keywords_path", target_keywords_path)
                else:
                    print(f"File must be a csv ({target_keywords_path.suffix})")
            else:
                print(f"Path does not exist: {target_keywords_path}")


# def analyze_gap(target_keywords_df, benchmark_keywords_df):
#     # logic
#     return


def main():
    target_keywords_df = get_target_keywords()
    #
    # analyze_gap(get_target_keywords())


if __name__ == "__main__":
    main()
