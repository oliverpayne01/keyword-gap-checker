import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import json


def create_config_file():
    global config

    with open("config.json", "w") as json_file:
        json.dump(config, json_file)


def save_config_file():
    global config

    with open("config.json", "w") as json_file:
        json.dump(config, json_file)


def set_config(key, value):
    global config

    if config != None:
        config[key] = value
    else:
        config = {key: value}


def load_config_file():
    config_path = "./config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as json_file:
            return json.load(json_file)
    else:
        return None


config = load_config_file()
# print(f"Config status: {config}")


def allow_save(key, value):
    allow_save_input = input(
        "Save selected target keywords path as default? (Y / N): "
    ).upper()

    if allow_save_input == "Y":
        set_config(key, value)

        if config == None:
            create_config_file()
        else:
            save_config_file()


def get_keywords_df(keyword_list):
    try:
        return pd.read_csv(config[f"{keyword_list}_keywords_path"])

    except (KeyError, TypeError):
        keywords_path = None

        def handle_input():
            nonlocal keywords_path
            keywords_path = Path(
                input(f"Enter the path to {keyword_list} keywords (must be a .csv): ")
            )

            validate_path()

        def validate_path():
            print(keywords_path)

            if os.path.exists(keywords_path):
                if keywords_path.suffix == ".csv":
                    allow_save(f"{keyword_list}_keywords_path", str(keywords_path))
                    return
                else:
                    print(f"File must be a csv ({keywords_path.suffix})")
            else:
                print(f"Path does not exist: {keywords_path}")

            handle_input()

        handle_input()

        return pd.read_csv(keywords_path)


# def analyze_gap(target_keywords_df, benchmark_keywords_df):
#     # logic
#     return


def main():
    target_keywords_df = get_keywords_df("target")
    benchmark_keyword_df = get_keywords_df("benchmark")
    print(benchmark_keyword_df.head())
    # analyze_gap(get_target_keywords())


if __name__ == "__main__":
    main()
