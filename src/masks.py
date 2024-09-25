import logging
import os

# Запуск pytest происходит из корневой директории проекта, а запуск срипта из директории src.
# Эта конструкция нужна для выравнивания путей.
path = ""
if os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1":
    path = "logs/masks.log"
elif os.getcwd() == "/Users/stanislavmayatsky/python/Skypro/myprojects/myproject1/src":
    path = "../logs/masks.log"

# Базовые настройки логгера
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    if "-" in card_number:
        card_number = card_number.replace("-", "")

    if " " in card_number:
        card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        logger.error(f"Номер карты {card_number} содержит недопустимые символы.")
        raise ValueError("Номер карты должен содержать цифры от 0 до 9")

    if len(card_number) != 16:
        logger.error(f"Номер карты {card_number} имеет недопустимую длину.")
        raise ValueError("Номер карты должен иметь длину 16 символов.")

    modified_card_number = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
    logger.info(f"Маска для номера карты {card_number} создана.")
    return modified_card_number[:7] + "** **** " + modified_card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if "-" in account_number:
        account_number = account_number.replace("-", "")

    if " " in account_number:
        account_number = account_number.replace(" ", "")

    if not account_number.isdigit():
        logger.error(f"Номер счёта {account_number} содержит недопустимые символы.")
        raise ValueError("Номер счёта должен содержать цифры от 0 до 9")

    if len(account_number) != 20:
        logger.error(f"Номер счёта {account_number} имеет недопустимую длину.")
        raise ValueError("Номер счёта должен иметь длину 20 символов.")

    logger.info(f"Маска для номера счёта {account_number} создана.")
    return "**" + account_number[-4:]


if __name__ == "__main__":
    print(get_mask_account("12345678912345678912"))
    print(get_mask_card_number("1234567891234567"))
