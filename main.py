# import src.masks as mk
# print(mk.get_mask_account("73654108430135874305"))
from collections.abc import Iterable

import src.category_bank_operation as operat
import src.category_bank_operation as bank_operations
import src.generators as gen
import src.processing as filter_data
import src.widget as wd


def greeting():
    """Функция приветствия и выбор файла с данными"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    flag_transaction = True
    while flag_transaction:
        user_input_info_transactions = input(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )

        if user_input_info_transactions == "1":
            print("Для обработки выбран JSON-файл.")
            flag_transaction = False
        elif user_input_info_transactions == "2":
            print("Для обработки выбран CSV-файл.")
            flag_transaction = False
        elif user_input_info_transactions == "3":
            print("Для обработки выбран XLSX-файл.")
            flag_transaction = False
        else:
            print("Введите значение от 1 до 3")


def status_filtrations_operations():
    """Функция фильтрации операций по статусу"""
    our_dict = {}
    flag_filtration = True
    while flag_filtration:
        user_input_status = input(
            " Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        if user_input_status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            our_dict = operat.process_bank_search(gen.transactions, user_input_status.upper())

            flag_filtration = False

        else:
            print(f"Статус операции '{user_input_status}' недоступен")
    return our_dict


def sort_operations():
    """Функция сортировки операций по дате,
    убыванию или возрастанию"""
    dict_status_filtrations_transactions = status_filtrations_operations()
    dict_transactions_data = {}
    flag_sort_data = True
    while flag_sort_data:
        date_user_unput_sort = input("Отсортировать операции по дате? Да/Нет\n")
        if date_user_unput_sort.lower() == "да":

            flag_ascending = True
            while flag_ascending:
                ascending_user_unput_sort = input("Отсортировать по возрастанию или по убыванию?\n")
                if ascending_user_unput_sort.lower() == "по убыванию":
                    dict_transactions_data = filter_data.sort_by_date(dict_status_filtrations_transactions)
                    flag_ascending = False

                elif ascending_user_unput_sort.lower() == "по возрастанию":
                    dict_transactions_data = filter_data.sort_by_date(dict_status_filtrations_transactions, date=False)
                    flag_ascending = False

            flag_sort_data = False
        elif date_user_unput_sort.lower() == "нет":
            break
    return dict_transactions_data


def is_generator(obj):
    """Функция, которая проверяет, является ли объект генератором"""
    return isinstance(obj, Iterable) and not isinstance(obj, list)


def sort_current_dict_currency():
    """Функция сортировки операций по номиналу либо по слову"""
    our_dict_currency = sort_operations()
    total_dict = {}
    flag = True
    while flag:
        currency_user_input_sort = input("Выводить только рублевые транзакции? Да/Нет\n")
        if currency_user_input_sort.lower() == "нет":
            flag_2 = True
            while flag_2:
                word_user_unput_sort = input(
                    "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
                )
                if word_user_unput_sort.lower() == "да":
                    input_sort_word = input("Введите слово для фильтрации: ")
                    total_dict = bank_operations.process_bank_search(our_dict_currency, input_sort_word)
                    flag = False
                    flag_2 = False
                elif word_user_unput_sort.lower() == "нет":
                    total_dict = our_dict_currency
                    flag = False
                    flag_2 = False

        elif currency_user_input_sort.lower() == "да":
            total_dict = gen.filter_by_currency(our_dict_currency, "rub")

            flag = False

    print("Распечатываю итоговый список транзакций...\n")

    transactions = total_dict  # или просто список
    if transactions:
        if is_generator(transactions):
            transactions = list(transactions)
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        for item in transactions:
            print(
                f'{wd.get_date(item["date"])} {item["description"]}\n'
                f'{wd.mask_account_card(item["from"])} -> {wd.mask_account_card(item["to"])}\n'
                f'Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'
            )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main():
    """Функция, которая отвечает за основную логику проекта и
    связывает функциональности между собой"""
    greeting()
    sort_current_dict_currency()


main()
