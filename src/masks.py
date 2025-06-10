import logging
from typing import Union

logging.basicConfig(
    filename="masks.log",
    format="%(asctime)s %(filename)s %(levelname)s %(message)s",
    filemode="w",
    level=logging.DEBUG,
)
logger = logging.getLogger()


def get_mask_card_number(card_number_client: Union[str]) -> str:
    """Функция, которая принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""

    if len(card_number_client) > 16 or len(card_number_client) < 16:
        logger.info("Incorrect card number")
        return "Некорректный номер карты"

    if not card_number_client.isdigit():
        logger.error("Enter the numeric value of the card number")
        raise TypeError("Введите числовое значение номера карты")

    logger.info("Everything was successful, the card number is correct")
    return f"{card_number_client[:4]} {card_number_client[4:6]}** **** {card_number_client[-4:]}"


def get_mask_account(number_account_client: Union[str]) -> str:
    """Функция, которая принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""

    if len(number_account_client) > 20 or len(number_account_client) < 20:
        logger.error("incorrect account number")
        return "Некорректный номер счета"

    if not number_account_client.isdigit():
        logger.error("Enter the numeric value of account number")
        raise TypeError("Введите числовое значение счета")
    logger.info("Everything was successful, the account number is correct")
    return f"**{number_account_client[-4:]}"


if __name__ == "__main__":
    logger.info("Start work function get_mask_card_number")
    user_input_number_card = "1234567894561232"
    result_number_card = get_mask_card_number(user_input_number_card)
    print(result_number_card)
    logger.info("Completed work function get_mask_card_number")

    logger.info("Start work function get_mask_account")
    account = "47700079228960636115"
    res = get_mask_account(account)
    print(res)
    logger.info("Completed work function get_mask_account")
