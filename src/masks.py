from typing import Any


def get_mask_card_number(card_number_client: Any) -> Any:
    """Функция, которая принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    part_1 = card_number_client[:4]
    part_2 = card_number_client[4:8]
    part_3 = card_number_client[9:13]
    part_4 = card_number_client[-4:]
    repl_1 = part_2.replace(part_2[2], "*")
    repl_2 = repl_1.replace(repl_1[3], "*")

    repl_3 = part_3.replace(part_3[0], "*")
    repl_4 = repl_3.replace(repl_3[1], "*")

    repl_5 = repl_4.replace(repl_4[2], "*")
    repl_6 = repl_5.replace(repl_5[3], "*")
    concat = f"{part_1} {repl_2} {repl_6} {part_4}"



    return concat


user_input_number_card = "7000792289606361"
result_number_card = get_mask_card_number(user_input_number_card)
print(result_number_card)


def get_mask_account(number_account_client: Any) -> Any:
    """Функция, которая принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    number = number_account_client[-6:]
    replace_two_1 = number.replace(number[0], "*")
    replace_two_2 = replace_two_1.replace(replace_two_1[1], "*")

    return replace_two_2


account = "73654108430135874305"
res = get_mask_account(account)
print(res)
