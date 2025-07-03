import re
from collections import Counter

from src.generators import transactions


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая принимает список словарей
    с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка"""
    dict_into_str = str(data)
    pattern = re.compile(search)
    result_search = re.findall(pattern, dict_into_str)
    our_list = []
    if result_search:
        for item_dict in data:
            our_keys = list(item_dict.keys())
            our_values = list(item_dict.values())
            if result_search[0] in our_values or result_search[0] in our_keys:

                our_list.append(item_dict)
    return our_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, принимающая список словарей с данными об операциях и список категорий,
    а возвращает количество операций в каждой категории"""
    our_dict = []
    for item_dict in data:
        if item_dict.get("description") in categories:
            our_dict.append(item_dict.get("description"))
    return Counter(our_dict)


if __name__ == "__main__":
    input_search = "EXECUTED"
    result = process_bank_search(transactions, input_search)
    print(result)
    category_operations = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]

    print(process_bank_operations(transactions, category_operations))
