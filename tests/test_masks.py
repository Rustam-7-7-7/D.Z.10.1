import pytest

from src.masks import get_mask_card_number, get_mask_account



def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == 7000 79** **** 6361

#Пример работы функции: 7000792289606361 # входной аргумент 7000 79** **** 6361 # выход функции



def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == **4305

#Пример работы функции: 73654108430135874305 # входной аргумент **4305 # выход функции



