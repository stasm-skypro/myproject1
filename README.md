# Домашняя работа к модулю 13.2
## Задачи
### Реализовать часть логики, предполагающую работу с регулярными выражениями.
1. Функция <> принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у которых в описании есть данная строка.
2. Функция <> принимает список словарей с данными о банковских операциях и список категорий операций. Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
3. Функция main в модуле main отвечает за основную логику проекта и связывает функциональности между собой.

### Пример работы функции main
**Программа приветствует пользователя:**

>Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями.
Выберите необходимый пункт меню:
>1. Получить информацию о транзакциях из JSON-файла
>2. Получить информацию о транзакциях из CSV-файла
>3. Получить информацию о транзакциях из XLSX-файла

>Пользователь: 1*

>Программа: Для обработки выбран JSON-файл.*

**После пользователь выбирает статус интересующих его операций.**

>Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

>Пользователь: EXECUTED

>Программа: Операции отфильтрованы по статусу "EXECUTED"

**В случае, если пользователь ввел неверный статус, программа не должна падать в ошибку, а должна возвращать пользователя к вводу корректного статуса:**
>Пользователь: test

>Программа: Статус операции "test" недоступен.

>Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

**После фильтрации программа выводит следующие вопросы для уточнения выборки операций, необходимых пользователю, и выводит в консоль операции, соответствующие выборке пользователя:**

>Программа: Отсортировать операции по дате? Да/Нет

>Пользователь: да

>Программа: Отсортировать по возрастанию или по убыванию? 

>Пользователь: по возрастанию/по убыванию

>Программа: Выводить только рублевые тразакции? Да/Нет

>Пользователь: да

>Программа: Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет

>Пользователь: да/нет

>Программа: Распечатываю итоговый список транзакций...

>Программа: Всего банковских операций в выборке: 4

>08.12.2019 Открытие вклада 
Счет **4321
Сумма: 40542 руб. 

>12.11.2019 Перевод с карты на карту
MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
Сумма: 130 USD

>18.07.2018 Перевод организации 
Visa Platinum 7492 65** **** 7202 -> Счет **0034
Сумма: 8390 руб.

>03.06.2018 Перевод со счета на счет
Счет **2935 -> Счет **4321
Сумма: 8200 EUR

**Если выборка оказалась пустой, программа выводит сообщение:**

>Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации

## Установка и использование.
Для запуска функций определённых в модулях проекта клонируем репозиторий:
##
        git clone git@github.com:stasm-skypro/myproject1.git

Переходим в папку с проектом, устанавливаем необходимые зависимости через poetry, используя файл pyproject.toml.
Находим модуль **main.py** и запускаем его.

Проект содержит готовые тесты для тестирования всех функций.
Тесты написаны с помощью библиотек **unittest** и **pytest**.

## Изменения и дополнения
(27.09.2024)
### Реализация поиска с помощью регулярных выражений
1. Реализована функция для поиска в списке словарей операций по заданной строке — описанию с использованием библиотеки 
re.
2. Функция для поиска в списке словарей операций по заданной строке принимает два аргумента: список с транзакциями и строку для поиска.
3. Функция для поиска в списке словарей операций по заданной строке использует библиотеку re для поиска.
4. Функция для поиска в списке словарей операций по заданной строке возвращает список словарей с операциями, у которых в описании есть строка, переданная аргументу функции.

### Реализация подсчета категорий
1. Реализована функция для подсчета количества банковских операций определенного типа.
2. Функция для подсчета количества банковских операций определенного типа принимает два аргумента: список с транзакциями и словарь для подсчета транзакций по описанию.
3. Функция для подсчета количества банковских операций определенного типа использует Counter из библиотеки collections.
4. Функция для подсчета количества банковских операций определенного типа возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.

### Сборка модулей
1. Написана функция main в модуле main, которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой.
2. Функция main предоставляет пользовательский интерфейс в соответствии с условиями задания.

### Тестирование
1. К новым функциональностям проекта написаны тесты.
2. Функциональный код покрыт тестами на 80% и более.
3. При запуске тестов командой pytest все тесты завершаются успешно.

(24.09.2024)
### Работа с CSV- и Excel-файлами
1. Создан отдельный модуль для новых функций.
2. Реализована функция для считывания финансовых операций из CSV.
3. Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента.
4. Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями.
5. Реализована функция для считывания финансовых операций из Excel.
6. Функция для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве аргумента.
7. Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями.
8. Все необходимые для работы библиотеки добавлены в зависимости проекта.

### Тестирование
1. К функциональностям проекта написаны тесты.
2. Тесты для функции считывания финансовых операций из CSV используют Mock и patch.
3. Тесты для функции считывания финансовых операций из Excel используют Mock и patch.
4. Функциональный код покрыт тестами на 80% и больше.


(23.09.24)

### Логирование модуля utils
1. Создан отдельный объект логгера для модуля utils.
2. Настроен file_handler для логгера модуля utils.
3. Настроен file_formatter для логгера модуля utils.
4. Формат записи логов включает метку времени, название модуля, уровень серьезности и сообщение.
5. Установлен форматер для логгера модуля utils.
6. Добавлен handler для логгера модуля utils.
7. Установлен уровень логирования для логгера модуля utils не меньше, чем DEBUG.
8. Логирование включено в успешные случаи использования функций модуля utils.
9. Логирование включено в ошибочные случаи использования функций модуля utils.
10. Логирование ошибочных случаев использования функций модуля utils производится с уровнем не ниже ERROR.


### Логирование модуля masks
1. Создан отдельный объект логгера для модуля masks.
2. Настроен file_handler для логгера модуля masks.
3. Настроен file_formatter для логгера модуля masks.
4. Формат записи логов включает метку времени, название модуля, уровень серьезности и сообщение.
5. Установлен форматер для логгера модуля masks.
6. Добавлен handler для логгера модуля masks.
7. Установлен уровень логирования для логгера модуля masks не меньше, чем DEBUG.
8. Логирование включено в успешные случаи использования функций модуля masks.
9. Логирование включено в ошибочные случаи использования функций модуля masks.
10. Логирование ошибочных случаев использования функций модуля masks производится с уровнем не ниже ERROR.


(20.09.2024)

### Обработка JSON-файла
1. Файл с банковскими операциями размещен в директории data в корне проекта.
2. Создан модуль utils в пакете src.
3. Реализована функция чтения JSON-файла в модуле utils.
4. Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента.
5. Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях.
6. Если JSON-файл пустой, содержит несписок или не найден, возвращается пустой список.

### Операции по конвертации валюты
1. Реализована функция конвертации валюты из USD и EUR в рубли.
2. Функция конвертации валюты из USD и EUR в рубли принимает на вход словарь с данными о транзакции.
3. Функция конвертации валюты из USD и EUR в рубли возвращает сумму транзакции (ключ amount) в рублях, тип данных float.
4. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.

### Сокрытие чувствительных данных
1. Ключи для авторизации в API конвертации валют скрыты в файле .env.
2. Собран шаблон файла .env с указанием названий всех переменных, необходимых для работы приложения.

### Тестирование
1. Написаны тесты к новым функциональностям проекта.
2. Тесты для функций конвертации валюты и открытия JSON-файла используют Mock и patch.
3. Функциональный код покрыт тестами на 80% и больше.
4. При запуске тестов командой pytest все тесты завершаются успешно.

### Оформление кода
1. При запуске линтера Flake8 выдается не более 5 ошибок.
2. Для всех реализованных функций написаны docstring.
3. Нейминг функций отвечает правилам оформления кода PEP8.
4. При вызове isort форматируется не более 1 импорта.

## Документация и ссылки.
Полное описание домашнего задания и ТЗ к функциям находятся по [ссылке](https://my.sky.pro/student-cabinet/stream-lesson/135686/homework-requirements).

## Лицензия.
Скрипты из данного модуля распространяются в познавательных целях, интеллектуальной ценности не имеют и предназначены для свободного копирования кем угодно.
