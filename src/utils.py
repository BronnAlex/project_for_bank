import json
import logging
import os

logging.basicConfig(
    filename="utils.log",
    format="%(asctime)s %(filename)s %(levelname)s %(message)s",
    filemode="w",
    level=logging.DEBUG,
)
logger = logging.getLogger()


def operation_bank_data_json(file_json):
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""

    # текущая директория
    current_dir = os.getcwd()
    # Получаем путь к родительской директории
    parent_dir = os.path.dirname(current_dir)
    path_to_file = os.path.join(parent_dir + "\\data\\" + file_json)
    logger.info(f"Got the file path {file_json}")
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                logger.info("Opened and read the contents of the file")
            except json.JSONDecodeError as js_ex:
                logger.error(f"Decoding error {js_ex}")

                return []
    except FileNotFoundError as f_not:
        logger.error(f"File not found {f_not}")

        return []
    return data


if __name__ == "__main__":
    logger.info("Start work function")
    result = operation_bank_data_json("operations.json")
    print(result)
    logger.info("Completion of work")
