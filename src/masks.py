def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера."""
    if "-" in card_number:
        card_number = card_number.replace("-", "")

    if " " in card_number:
        card_number = card_number.replace(" ", "")

    if len(card_number) != 16:
        raise ValueError("Номер карты должен иметь длину 16 символов.")

    modified_card_number = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
    return modified_card_number[:7] + "** **** " + modified_card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if "-" in account_number:
        account_number = account_number.replace("-", "")

    if " " in account_number:
        account_number = account_number.replace(" ", "")

    if len(account_number) != 20:
        raise ValueError("Номер счёта должен иметь длину 20 символов.")

    return "**" + account_number[-4:]
