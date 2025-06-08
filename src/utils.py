import json
import os


def operation_bank_data_json(file_json):
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    # текущая директория
    current_dir = os.getcwd()
    # Получаем путь к родительской директории
    parent_dir = os.path.dirname(current_dir)
    path_to_file = os.path.join(parent_dir + "\\data\\" + file_json)
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("Ошибка декодирования")
                return []
    except FileNotFoundError:
        print(f"Файл не найден {path_to_file}")
        return []
    return data


if __name__ == "__main__":

    result = operation_bank_data_json("operations.json")
    print(result)
