import pytest

from src.widget import mask_account_card, get_date

def test_mask_account_card():
    assert mask_account_card(Visa Platinum 7000792289606361) == Visa Platinum 7000 79** **** 6361


def test_get_date():
    assert get_date(2024-03-11T02:26:18.671407) == 11.03.2024


# Примеры работы функции
# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции
#
# # Пример для счета
# Счет 73654108430135874305  # входной аргумент
# Счет **4305  # выход функции


# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305

