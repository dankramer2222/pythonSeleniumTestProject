import pytest


def add_two_numbers(a,b):
    return a+b


@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1,2) == 3, "The sum of a and b shoud be 3"


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100,300) == 400, "The sum of a and b shoud be 400"

