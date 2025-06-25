import pandas as pd
import csv
import json
from pathlib import Path


def reading_file_csv(path_csv):
    file_path = path_csv / "transactions.csv"
    absolute_path = file_path.resolve()
    try:
        df = pd.read_csv(absolute_path, sep=";")
        js_dict = df.to_dict(orient="records")
        return json.dumps(js_dict, ensure_ascii=False, indent=4)

    except FileNotFoundError as file:
        print(f"Файл {file} не найден")
    return None




if __name__ == "__main__":
    home_dir = Path.cwd()
    result_read_csv = reading_file_csv(home_dir)
    print(result_read_csv)