import json
import logging
import os

# Запуск pytest происходит из корневой директории проекта, а запуск срипта из директории src.
# Эта конструкция нужна для выравнивания путей.
path = ""
if os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1":
    path = "logs/utils.log"
elif os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1/src":
    path = "../logs/utils.log"

# Базовые настройки логгера
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file(file_path: str) -> list[dict | None]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Пример использования:
    result = read_file(path_to_operations)
    """
    # Если файл, указанный в переменной file_path не существует, то вернуть пустой список.
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        logger.info(f"Файл {file_path} открыт на чтение.")
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не существует.")
        return []

    # Если json-файл пустой, то вернуть пустой список.
    try:
        data = json.loads(content)
        logger.info(f"Данные из файла {file_path} прочитаны.")
    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения json из файла {file_path}.")
        return []

    # Если содержимое файла не является списком (содержит несписок), то вернуть пустой список.
    if not isinstance(data, list):
        logger.error(f"одержимое файла {file_path} не является объектом типа list.")
        return []

    return data


if __name__ == "__main__":
    print(read_file("../data_for_tests/operations_empty_sample.json"))
