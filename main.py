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


def get_target_keywords():
    try:
        return pd.read_csv(config["target_keywords_path"])

    except (KeyError, TypeError):
        target_keywords_path = None

        def handle_input():
            nonlocal target_keywords_path
            target_keywords_path = Path(
                input("Enter the path to target keywords (must be a .csv): ")
            )

            validate_path()

        def validate_path():
            print(target_keywords_path)

            if os.path.exists(target_keywords_path):
                if target_keywords_path.suffix == ".csv":
                    allow_save("target_keywords_path", str(target_keywords_path))
                    return
                else:
                    print(f"File must be a csv ({target_keywords_path.suffix})")
            else:
                print(f"Path does not exist: {target_keywords_path}")

            handle_input()

        handle_input()

        return pd.read_csv(target_keywords_path)


# def analyze_gap(target_keywords_df, benchmark_keywords_df):
#     # logic
#     return


def main():
    target_keywords_df = get_target_keywords()
    print(target_keywords_df.head())
    #
    # analyze_gap(get_target_keywords())


if __name__ == "__main__":
    main()
