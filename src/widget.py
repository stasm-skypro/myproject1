from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Принимает один аргумент — строку, содержащую тип и номер карты или счета. Возвращает строку с замаскированным \
    номером."""
    if not card or card == " ":
        raise ValueError("Поле с номером карты не должно быть пустым!")

    *account_type, account_number = card.split()

    if " ".join(account_type).lower() not in (
        "maestro",
        "mastercard",
        "visa classic",
        "visa platinum",
        "счёт",
        "счет",
    ):
        raise ValueError("Поле с номером карты должно быть правильно заполнено!")

    if not account_number.isdigit():
        raise ValueError("Поле с номером карты должно быть правильно заполнено!")

    encrypted_account_number = ""

    # Если мы точно знаем, что номер карты всегда содержит 16 цифр, а номер счёта - 20 цифр, то
    # длинна этого номера и будет критерием выбора.
    if len(account_number) == 16:  # Это номер карты
        encrypted_account_number = get_mask_card_number(account_number)

    if len(account_number) == 20:  # Это номер счёта
        encrypted_account_number = get_mask_account(account_number)

    return " ".join([*account_type]) + " " + encrypted_account_number


def get_date(current_date: str) -> str:
    """Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в \
    формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    year, month, day = tuple(current_date[:11].split("-"))
    return ".".join([day.replace("T", ""), month, year])
