import pandas as pd
import csv
import json


def reading_file_csv(path_csv):
    try:
        with open(path_csv, "r", encoding="utf-8") as file_csv:
            read_csv = csv.DictReader(file_csv, delimiter=";")
            for row in read_csv:
                print(f"Операцию произвел: {row['from']}. Средства получил: {row['to']}. Действие: {row['description']}")

    except FileNotFoundError as file:
        print(f"Файл {file} не найден")
    return None



if __name__ == "__main__":
    result_read_csv = reading_file_csv("transactions.csv")
    print(result_read_csv)