import json
import os

def operation_bank_data_json(path_to_file):
    try:
        with open(path_to_file, "r", encoding='utf-8') as file:
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
    file_json = "operations.json"
    # текущая директория
    current_dir = os.getcwd()
    # Получаем путь к родительской директории
    parent_dir = os.path.dirname(current_dir)
    result = operation_bank_data_json(parent_dir+"\\data\\"+file_json)
    print(result)
