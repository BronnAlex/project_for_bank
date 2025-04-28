# Аргументом может быть строка типа
# Visa Platinum 7000792289606361
# Maestro 7000792289606361
# Счет 73654108430135874305
# Возвращать строку с замаскированным номером.
# Для карт и счетов используйте разные типы маскировки.
# Переиспользуйте уже существующие функции маскировки из вашего проекта,
# чтобы избежать дублирования кода.

               # Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции
               # Пример для счета
# Счет 73654108430135874305  # входной аргумент
# Счет **4305  # выход функции


def mask_account_card(account_card):
    """Функция, принимающая карту или счет с их названиями и возвращает соответствующую маску"""
    list1 = []
    card_string = ''
    for symbol in account_card:
        if symbol.isdigit():
            card_string += symbol

    if len(card_string) == 16:
        card_mask_account = card_string[:4] + "*" * (len(card_string) - 10) + card_string[-4:]

        index_start = 0
        index_end = 4
        for _ in card_mask_account[:: 4]:
            list1.append(card_mask_account[index_start:index_end])
            index_start += 4
            index_end += 4

        total_result = ' '.join(list1)
        return account_card[0:-16] + total_result

    elif len(card_string) == 20:
        mask_account =  "*" * (len(card_string) - 18) + card_string[-4:]

        return mask_account


user_input_card = 'Maestro 7000792289606361'

result_mask_card = mask_account_card(user_input_card)
print(result_mask_card)