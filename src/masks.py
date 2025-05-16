from typing import Union


def get_mask_card_number(card_number_client: str) -> str:
    """Функция, которая принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""



    if len(card_number_client) > 16 or len(card_number_client) < 16:
        return "Некорректный номер карты"

    # if not card_number_client.isdigit():
    #     raise TypeError("Введите числовое значение")

    return f"{card_number_client[:4]} {card_number_client[4:6]}** **** {card_number_client[-4:]}"


def get_mask_account(number_account_client: Union[str]) -> str:
    """Функция, которая принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    if len(number_account_client) > 20 or len(number_account_client) < 20:
        return "Некорректный номер счета"
    return f"**{number_account_client[-4:]}"


if __name__ == "__main__":
    user_input_number_card = ""
    result_number_card = get_mask_card_number(user_input_number_card)
    print(result_number_card)

    account = "73654108430135874305"
    res = get_mask_account(account)
    print(res)
