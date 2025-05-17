from typing import Any

from src.masks import get_mask_account as mask_account
from src.masks import get_mask_card_number as mask_card


def mask_account_card(account_card: Any) -> Any:
    """Функция, принимающая карту или счет с их названиями
    и возвращает соответствующую маску"""
    card_string = ""
    for symbol in account_card:
        if symbol.isdigit():
            card_string += symbol

    if len(card_string) == 16:
        current_card = mask_card(card_string)
        return account_card[0:-16] + current_card

    elif len(card_string) == 20:
        current_account = f'{account_card[0:4]} {mask_account(card_string)}'

        return current_account
    return "Неверно введены данные"


def get_date(current_date: Any) -> Any:
    """Функция, принимающая дату и возвращающая её в нужном формате"""
    if current_date:
        repl_1 = current_date.replace("-", ".")
        repl_2 = repl_1.replace("-", ".")
        take_date = repl_2[:10]
        our_date = ".".join(reversed(take_date.split(".")))
        return our_date
    return "Введите дату"


if __name__ == "__main__":
    user_input_card = "47700079228960636115"
    result_mask_card = mask_account_card(user_input_card)
    print(result_mask_card)

    user_input_date = "2024-03-11T02:26:18.671407"
    result_get_date = get_date(user_input_date)
    print(result_get_date)
