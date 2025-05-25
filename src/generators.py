import random
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264452,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264452,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264452,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def filter_by_currency(transaction_list, current_value):
    """ Функция-генератор, который принимает на вход список словарей, представляющих транзакции.
        Возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    for item in transaction_list:
        if item.get("operationAmount", {}).get("currency", {}).get("code", {}) == current_value:
            yield item


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions, {}))


def transaction_descriptions(transaction_list):
    """Функция-генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for item in transaction_list:
        yield item["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

# Выражение f"{num:016d}" — это f-строка (форматированная строка) в Python, где:
# 		• num — переменная (целое число),
# 		• :016d — спецификатор формата.
# Расшифровка :016d:
# 		• d — формат как целое десятичное число (integer),
# 		• 016 — общее количество символов = 16 цифр,
# 		•  — заполнить слева нулями, если число короче.
# Например:
# num = 42
# formatted = f"{num:016d}"
# print(formatted)  # 👉 '0000000000000042'
# for num in range(start, end): yield f"{num:04d} {num:04d} {num:04d} {num:04d}"

def card_number_generator(start, stop):
    """Функция-генератор, который выдает номера банковских карт в формате
        XXXX XXXX XXXX XXXX,  где Х - это рандомное число"""
    for num in range(start, stop + 1):
        number_card = f"{num:016d}"
        number_card_format = f"{number_card[0:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:16]}"
        yield number_card_format

for card_number in card_number_generator(1, 5):
    print(card_number)
