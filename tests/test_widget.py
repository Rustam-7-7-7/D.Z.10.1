import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_card():
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'


def test_mask_account_card_account():
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'


# Примеры работы функции
# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции
#
# # Пример для счета
# Счет 73654108430135874305  # входной аргумент
# Счет **4305  # выход функции


@pytest.mark.parametrize(
    "type_and_number, expected",
    [
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
        ('Счет 64686473678894779589', 'Счет **9589'),
        ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
        ('Счет 35383033474447895560', 'Счет **5560'),
        ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
        ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
        ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
        ('Счет 73654108430135874305', 'Счет **4305'),
    ]
)
def test_mask_account_card(type_and_number, expected):
    assert mask_account_card(type_and_number) == expected


# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305



def test_get_date():
    assert get_date('2025-03-11T02:26:18.671407') == '11.03.2025'


def test_get_date_leap_year():
    assert get_date('2024-02-29T07:46:58.771407') == '29.02.2024'


def test_get_date_empty():
    assert get_date('') == "Введено пустое значение."
