import json

from src.utils import operation_bank_data_json


def test_operation_bank_data_json():
    assert operation_bank_data_json("operations.json") == []


def test_operation_bank_data_json_error_1():

    try:
        operation_bank_data_json("jkjk")

    except FileNotFoundError as e:
        # Проверяем, что исключение было
        assert isinstance(e, FileNotFoundError)
        # Проверяем сообщение об ошибке
        assert "Ошибка декодирования"


def test_operation_bank_data_json_error_2():

    try:
        operation_bank_data_json("operations.json")
    except json.JSONDecodeError as e:
        # Проверяем, что исключение было
        assert isinstance(e, json.JSONDecodeError)
        # Проверяем сообщение об ошибке
        assert "Ошибка декодирования"
