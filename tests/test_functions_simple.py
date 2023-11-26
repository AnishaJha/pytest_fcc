import time

import pytest
import source.functions_simple as functions_simple


def test_add():
    result = functions_simple.add_numbers(2, 4)
    assert result == 6


def test_divide():
    result = functions_simple.divide_numbers(10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        functions_simple.divide_numbers(10, 0)


@pytest.mark.slow
def test_slow():
    time.sleep(5)
    result = functions_simple.divide_numbers(10, 2)
    assert result == 5


@pytest.mark.skip(reason="Broken test")
def test_add_new():
    result = functions_simple.add_numbers(2, 4)
    assert result == 6


@pytest.mark.xfail(reason="Error for divide by zero")
def test_divide_by_zero_n():
    functions_simple.divide_numbers(4, 0)
