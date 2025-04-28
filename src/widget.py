from typing import Union


def mask_account_card(account_card: Union[str]) -> str:
    """Функция, принимающая карту или счет с их названиями
    и возвращает соответствующую маску"""
    list1 = []
    card_string = ""
    for symbol in account_card:
        if symbol.isdigit():
            card_string += symbol

    if len(card_string) == 16:
        card_mask_account = card_string[:4] + "*" * (len(card_string) - 10) + card_string[-4:]

        index_start = 0
        index_end = 4
        for _ in card_mask_account[::4]:
            list1.append(card_mask_account[index_start:index_end])
            index_start += 4
            index_end += 4

        total_result = " ".join(list1)
        return account_card[0:-16] + total_result

    elif len(card_string) == 20:
        mask_account = "*" * (len(card_string) - 18) + card_string[-4:]

        return mask_account
    return "Неверно введены данные"


user_input_card = "Maestro 7000792289606361"

result_mask_card = mask_account_card(user_input_card)
print(result_mask_card)


def get_date(current_date: Union[str]) -> str:
    """Функция, принимающая дату и возвращающая её в нужном формате"""
    repl_1 = current_date.replace("-", ".")
    repl_2 = repl_1.replace("-", ".")
    take_date = repl_2[:10]
    our_date = ".".join(reversed(take_date.split(".")))
    return our_date


user_input_date = "2024-03-11T02:26:18.671407"
result_get_date = get_date(user_input_date)
print(result_get_date)
