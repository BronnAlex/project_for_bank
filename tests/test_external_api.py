from unittest.mock import patch

from src.external_api import get_transaction_amount_into_rub


@patch("requests.get")
def test_get_transaction_amount_into_rub(mock_get):
    mock_get.return_value.json.return_value = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert get_transaction_amount_into_rub(mock_get.return_value.json.return_value) == 31957.58
    # mock_get.assert_called_with("https://api.apilayer.com/exchangerates_data/convert?to=USD&from=RUB&amount=31957.58")
