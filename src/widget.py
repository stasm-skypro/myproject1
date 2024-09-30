import logging
import os

from src.masks import get_mask_account, get_mask_card_number

# Запуск pytest происходит из корневой директории проекта, а запуск срипта из директории src.
# Эта конструкция нужна для выравнивания путей.
path = ""
if os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1":
    path = "logs/widget.log"
elif os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1/src":
    path = "../logs/widget.log"


# Базовые настройки логгера
logger = logging.getLogger("widget")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_account_card(name: str) -> str:
    """Принимает один аргумент — строку, содержащую тип и номер карты или счета. Возвращает строку с замаскированным \
    номером."""
    if not name or name == " ":
        logger.error("Поле с номером карты или номером счёта пустое.")
        raise ValueError("Поле с номером карты или номером счёта не должно быть пустым!")

    *_type, _number = name.split()

    # Определяем какой объект передан: номер счёта или номер карты.
    # В наименовании сначала должен указываться тип объекта: счёт или название карты. Допустимые названия карт:
    # "maestro",
    # "mastercard",
    # "visa",
    # "visa classic",
    # "visa platinum",
    # написанные латинскими буквами в любом регистре.
    if " ".join(_type).lower() in ("счет", "счёт"):
        # Это счёт, вызываем функцию get_mask_account
        logger.info(f"{name} содержит имя и номер счёта. Маскируем номер.")
        encrypted_number = get_mask_account(_number)

    elif " ".join(_type).lower() in (
        "maestro",
        "mastercard",
        "visa",
        "visa classic",
        "visa platinum",
        "visa gold",
        "мир",
    ):
        # Это карта, вызываем функцию get_mask_card_number
        logger.info(f"{name} содержит имя и номер карты. Маскируем номер.")
        encrypted_number = get_mask_card_number(_number)

    else:
        # В названии счёта или карты ошибка (недопустимый тип)
        logger.error(f"Карта {name} имеет ошибку в названии.")
        raise ValueError("Поле карты должно быть правильно заполнено!")

    return " ".join([*_type]) + " " + encrypted_number


def get_date(current_date: str) -> str:
    """Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в \
    формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    year, month, day = tuple(current_date[:11].split("-"))
    return ".".join([day.replace("T", ""), month, year])


if __name__ == "__main__":
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
