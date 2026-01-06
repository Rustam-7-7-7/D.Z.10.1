import unittest

import pytest

from src.decorators import log, my_function


def test_log(capsys):
    my_function(10,2)
    captured = capsys.readouterr()
    assert captured.out ==