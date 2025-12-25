# Домашнее задание № 10.2
#############################################################################
account_number = input(f'Введите номер счёта: ')
card_number = input(f'Введите номер карты: ')


def get_mask_card_number(card_number: int) -> str:
    '''Функция, которая принимает на вход номер карты и возвращает ее маску.'''

    return f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"


print(get_mask_card_number(card_number))


def get_mask_account(account_number: int) -> str:
    '''Функция, которая принимает на вход номер счета и возвращает его маску.'''

    return f"**{account_number[-4:]}"


print(get_mask_account(account_number))

#############################################################################
