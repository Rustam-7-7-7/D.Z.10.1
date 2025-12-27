import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

#Пример работы функции: 7000792289606361 # входной аргумент 7000 79** **** 6361 # выход функции


def test_get_mask_card_number_short():
    assert get_mask_card_number('7000792289606') == '7000 79** **** 6'

#Пример работы функции: 7000792289606 # входной аргумент 7000 79** **** 6 # выход функции


def test_get_mask_card_number_long():
    assert get_mask_card_number('7000792289606361789') == '7000 79** **** 6361789'

#Пример работы функции: 7000792289606361789 # входной аргумент 7000 79** **** 6361789 # выход функции


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == ' ** **** '

#Пример работы функции:  # входной аргумент  ** **** # выход функции




def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'

#Пример работы функции: 73654108430135874305 # входной аргумент **4305 # выход функции


def test_get_mask_account_long():
    assert get_mask_account('73654108430135874305123') == '**5123'

# Пример работы функции: 73654108430135874305123 # входной аргумент **5123 # выход функции


def test_get_mask_account_short():
    assert get_mask_account('73654108430135874') == '**5874'

# Пример работы функции: 73654108430135874 # входной аргумент **5874 # выход функции
