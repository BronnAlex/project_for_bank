import os

import requests
from dotenv import load_dotenv

from src.utils import operation_bank_data_json

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amount_into_rub(transaction):
    """Возвращает сумму транзакции в рублях.
    Если валюта не RUB, конвертирует по текущему курсу через внешний API."""

    # Случай транзакции в рублях
    if transaction.get("operationAmount").get("currency").get("code") == "RUB":
        return float(transaction["operationAmount"]["amount"])

    # Случай транзакции в иной валюте
    elif transaction.get("operationAmount").get("currency").get("code"):
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers).json()
        return round(float(response["result"]), ndigits=2)

    return None


if __name__ == "__main__":
    file_json = "operations.json"
    input_dict_currency = operation_bank_data_json(file_json)
    result = get_transaction_amount_into_rub(input_dict_currency[0])

    print(result)
