import src.widget as wd

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
]
# """
# 08.12.2019 Открытие вклада
# Счет **4321
# Сумма: 40542 руб.
#
# 12.11.2019 Перевод с карты на карту
# MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# Сумма: 130 USD
# """

for item in transactions:
    print(
        f'{wd.get_date(item["date"])} {item["description"]}\n'
        f'{wd.mask_account_card(item["from"])} -> {wd.mask_account_card(item["to"])}\n'
        f'Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}'
    )
