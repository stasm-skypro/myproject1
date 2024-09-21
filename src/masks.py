import logging

# Базовые настройки логгера
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    if "-" in card_number:
        card_number = card_number.replace("-", "")

    if " " in card_number:
        card_number = card_number.replace(" ", "")

    if len(card_number) != 16:
        logger.debug(f"Номер карты {card_number} имеет неверную длину.")
        raise ValueError("Номер карты должен иметь длину 16 символов.")

    modified_card_number = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
    logger.debug("Маска для номера карты создана.")
    return modified_card_number[:7] + "** **** " + modified_card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if "-" in account_number:
        account_number = account_number.replace("-", "")

    if " " in account_number:
        account_number = account_number.replace(" ", "")

    if len(account_number) != 20:
        logger.debug(f"Номер карты {account_number} имеет неверную длину.")
        raise ValueError("Номер счёта должен иметь длину 20 символов.")

    logger.debug("Маска для номера счёта создана.")
    return "**" + account_number[-4:]
