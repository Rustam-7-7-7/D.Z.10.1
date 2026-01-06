import pytest

from src.decorators import log, my_function


def test_log(capsys):
    my_function(10,2)
    captured = capsys.readouterr()
    assert captured.out == ("Начало выполнения функции 'my_function' с аргументами (10, 2) и {}\n"
                            "Функция 'my_function' успешно завершена с результатом: 5.0\n"'\n')


def test_log_err(capsys):
    my_function(10, 0)
    captured = capsys.readouterr()
    assert captured.out == ("Начало выполнения функции 'my_function' с аргументами (10, 0) и {}\n"
                            "Функция 'my_function' завершилась с ошибкой: ZeroDivisionError, division by "'zero\n''\n')
