import pytest
from series.series import *

def test_fibonacci():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected
def test_fibonacci():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci2():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibonacci3():
    assert fibonacci(7) == 13



def test_lucas():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas2():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas3():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas4():
    actual = lucas(6)
    expected = 18
    assert actual == expected    


def test_sum_series():
    assert sum_series(2) == 1



