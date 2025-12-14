import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import json


def create_config():
    print("called create config")
    with open("config.json", "w") as json_file:
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
print(f"Config status: {config}")


def allow_save(key, value):
    allow_save_input = Path(
        input("Save selected target keywords path as default? (Y / N): ").upper()
    )
    if allow_save_input == "Y":
        print(f"User input: {allow_save_input}")
        if config == None:
            create_config()
        set_config(key, value)


def get_target_keywords():
    if config == None or not config["target_keywords_path"]:
        target_keywords_input = input(
            "Enter the path to target keywords (must be a .csv): "
        )
        target_keywords_path = Path(target_keywords_input)

        def validate_file():
            print(target_keywords_path)

            if os.path.exists(target_keywords_path):
                if target_keywords_path.suffix == ".csv":
                    allow_save("target_keywords_path", target_keywords_path)
                else:
                    print(f"File must be a csv ({target_keywords_path.suffix})")
            else:
                print(f"Path does not exist: {target_keywords_path}")

        validate_file()

        while (
            not os.path.exists(target_keywords_path)
            or target_keywords_path.suffix != ".csv"
        ):
            target_keywords_path = Path(target_keywords_input)
            validate_file()


# def analyze_gap(target_keywords_df, benchmark_keywords_df):
#     # logic
#     return


def main():
    target_keywords_df = get_target_keywords()
    #
    # analyze_gap(get_target_keywords())


if __name__ == "__main__":
    main()
