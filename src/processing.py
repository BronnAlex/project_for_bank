# -*- coding: utf-8 -*-
from typing import Any, Iterable, Union


def filter_by_state(our_list: Iterable[dict[str, Any]], state: Union[str] = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению state по умолчанию"""
    new_list_dicts = []
    for item_dicts in our_list:
        if item_dicts["state"] == state:
            new_list_dicts.append(item_dicts)
    return new_list_dicts


list_filter_by_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    result_state = filter_by_state(list_filter_by_state)
    print(result_state)
