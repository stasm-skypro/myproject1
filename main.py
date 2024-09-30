from src.utils import read_file
from src.processing import (
    filter_by_state,
    sort_by_date,
    filter_by_rub,
    find_transactions,
    group_transactions_by_category,
)
from src.widget import get_date, mask_account_card


def pretty_print(lst: list) -> None:
    """Функция распечатывает двумерный список по-строчно."""
    for row in lst:
        print(row)


def main() -> None:
    """Отвечает за основную логику проекта и связывает функциональности между собой."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    user_input = ""
    while user_input not in ["1", "2", "3"]:
        print("1. Получить информацию о транзакциях из JSON-файла.")
        print("2. Получить информацию о транзакциях из CSV-файла.")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input(">>>$: ")
    transactions_data = []
    match user_input:
        case "1":
            print("Для обработки выбран JSON-файл.")
            transactions_data = read_file("data/operations.json")
        case "2":
            print("Для обработки выбран CSV-файл.")
            transactions_data = read_file("data/transactions.csv")
        case "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_data = read_file("data/transactions_excel.xlsx")

    # Фильтрация списка транзакций по статусу, который задал пользователь.
    state = ""
    while 1:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.")
        user_input = input("\n>>>$: ").upper()
        if user_input.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print("Статус операции '{}' недоступен.".format(user_input))
        else:
            state = user_input.upper()
            break
    transactions_data = filter_by_state(transactions_data, state)

    # Сортировка списка транзакций по дате, если пользователь выбрал этот критерий.
    do_sort_by_date = 0
    user_input = input("Отсортировать операции по дате? Да/Нет\n>>>$: ")
    if user_input.lower() == "да":
        do_sort_by_date = 1

    user_input = input("Отсортировать по возрастанию (нажмите 0) или по убыванию (нажмите 1)?\n>>>$: ")
    if user_input.lower() == "по возрастанию":
        sorting_order = 0
    else:
        sorting_order = 1
    if do_sort_by_date:
        transactions_data = sort_by_date(transactions_data, sorting_order)

    user_input = input("Выводить только рублевые транзакции? Да/Нет\n>>>$: ")
    if user_input.lower() == "да":
        transactions_data = filter_by_rub(transactions_data)

    do_filter_by_description = 0
    user_input = input("Отфильтровать список транзакций по описанию? Да/Нет\n>>>$: ")
    if user_input.lower() == "да":
        do_filter_by_description = 1

    if do_filter_by_description:
        user_input = input("Какие именно операции отразить в списке транзакций?\n>>>$:  ")
        transactions_data = find_transactions(transactions_data, user_input)

    if not transactions_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    grouped_transactions = group_transactions_by_category(transactions_data)
    operations_count = sum(v for k, v in grouped_transactions.items())
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке:", operations_count)
    print()
    for transaction in transactions_data:
        print(f"{get_date(transaction["date"])} {transaction["description"]}")
        print(f"{mask_account_card(transaction["to"])}")
        print(f"{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}")
        print()


if __name__ == "__main__":
    main()
