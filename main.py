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
        user_input = input(
            "1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n>>>$:"
        )
    match user_input:
        case "1":
            print("Для обработки выбран JSON-файл.")
        case "2":
            print("Для обработки выбран CSV-файл.")
        case "3":
            print("Для обработки выбран XLSX-файл.")

    state = ""
    while 1:
        user_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n>>>$:"
        ).upper()
        if user_input.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print("Статус операции '{}' недоступен.".format(user_input))
        else:
            state = user_input.upper()
            break

    sorting_criteria = []
    user_input = input("Отсортировать операции по дате? Да/Нет\n>>>$:")
    if user_input.lower() in ["да", "yes", "y"]:
        sorting_criteria.append("bydate")

    user_input = input("Отсортировать по возрастанию или по убыванию?\n>>>$")
    if user_input.lower() == "по возрастанию":
        sorting_criteria.append("increasy")

    user_input = input("Выводить только рублевые тразакции? Да/Нет\n>>>$")
    if user_input.lower() in ["да", "yes", "y"]:
        sorting_criteria.append("onlyrub")

    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if user_input.lower() in ["да", "yes", "y"]:
        sorting_criteria.append("Перевод со счета на счет")

    operations_count = 0
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке:", operations_count)


if __name__ == "__main__":
    main()
