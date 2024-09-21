import unittest

from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


class Tests(unittest.TestCase):

    def test11(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <тип карты> <номер карты>."""
        self.assertEqual(mask_account_card("Maestro 1596837868705199"), "Maestro 1596 83** **** 5199")

    def test12(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <тип карты> <номер карты>."""
        self.assertEqual(
            mask_account_card("MasterCard 7158300734726758"),
            "MasterCard 7158 30** **** 6758",
        )

    def test13(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <тип карты> <номер карты>."""
        self.assertEqual(
            mask_account_card("MasterCard 7158300734726758"),
            "MasterCard 7158 30** **** 6758",
        )

    def test14(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <тип карты> <номер карты>."""
        self.assertEqual(
            mask_account_card("Visa Classic 6831982476737658"),
            "Visa Classic 6831 98** **** 7658",
        )

    def test15(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <тип карты> <номер карты>."""
        self.assertEqual(
            mask_account_card("Visa Platinum 8990922113665229"),
            "Visa Platinum 8990 92** **** 5229",
        )

    def test21(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <номер счёта>."""
        self.assertEqual(mask_account_card("Счет 64686473678894779589"), "Счет **9589")

    def test22(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <номер счёта>."""
        self.assertEqual(mask_account_card("Счет 35383033474447895560"), "Счет **5560")

    def test23(self) -> None:
        """Тестирует функцию mask_account_card с аргументом <номер счёта>."""
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет **4305")

    def test31(self) -> None:
        """Тестирует функцию get_date."""
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")

    def test41(self) -> None:
        """Выход функции со статусом по умолчанию 'EXECUTED'"""
        self.assertEqual(
            filter_by_state(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ),
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )

    def test42(self) -> None:
        """Выход функции, если вторым аргументов передано 'CANCELED'"""
        self.assertEqual(
            filter_by_state(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                "CANCELED",
            ),
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )

    def test51(self) -> None:
        """Выход функции (сортировка по убыванию, т.е. сначала самые последние операции)"""
        self.assertEqual(
            sort_by_date(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            ),
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )

    def test52(self) -> None:
        """Выход функции (сортировка по возрастанию, т.е. сначала самые старые операции)"""
        self.assertEqual(
            sort_by_date(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                0,
            ),
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ][::-1],
        )
