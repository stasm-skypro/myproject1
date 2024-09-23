# Домашняя работа к модулю 12.2
## Задачи
### Реализовать логирование в текущем проекте, используйте для этого библиотеку logging.

1. Создать логгеры для модулей: masks, utils.
2. Реализовать запись логов в файл. Логи должны записываться в папку logs в корне проекта. Файлы логов должны иметь расширение .log .
3. Формат записи лога в файл должен включать метку времени, название модуля, уровень серьезности и сообщение, описывающее событие 
или ошибку, которые произошли.
4. Лог должен перезаписываться при каждом запуске приложения.

## Установка и использование.
Для запуска функций определённых в модулях проекта клонируем репозиторий:
##
        git clone git@github.com:stasm-skypro/myproject1.git

Переходим в папку с проектом, устанавливаем необходимые зависимости через poetry, используя файл pyproject.toml.
Находим модуль **main.py** и запускаем его.

Проект содержит готовые тесты для тестирования всех функций.
Тесты написаны с помощью библиотек **unittest** и **pytest**.

## Изменения и дополнения
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
