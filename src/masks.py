# Домашнее задание № 12.2
#############################################################################


def get_mask_card_number(card_number: int, success=True) -> str:
    '''Функция, которая принимает на вход номер карты и возвращает ее маску.'''

    if success:
        logger.info('Function executed successfully.')
    else:
        logger.error('An error occurred in the function.')

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    '''Функция, которая принимает на вход номер счета и возвращает его маску.'''

    return f"**{account_number[-4:]}"


# Логирование
import logging

logger = logging.getLogger('masks')

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/masks.log', mode='w')

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

# Пример использования логера
card_number = input(f'Введите номер карты: ')

print(get_mask_card_number(card_number, success=True))

print(get_mask_card_number(card_number, success=False))

#############################################################################
