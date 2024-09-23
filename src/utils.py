import json
import logging

# Базовые настройки логгера
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w")
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


# if __name__ == "__main__":
#     path_to_operations = "../data/operations.json"
#     result = read_file(path_to_operations)
#     print(result)
#
#     current_transaction = {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560",
#     }
