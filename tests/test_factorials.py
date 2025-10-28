from main import factorials
import pytest


def test_positive_numbers():
    """sprawdza poprawnosc funkcji przy liczbie dodatniej jako argument"""
    result = list(factorials(5))
    assert result == [1, 2, 6, 24, 120]


def test_negative_numbers():
    """sprawdza poprawnosc funkcji przy liczbie ujemnej jako argument"""
    result = list(factorials(-3))
    assert result == []


def test_zero():
    """sprawdza poprawnosc funkcji 0 jako argument"""
    result = list(factorials(0))
    assert result == [2, 5]


def test_float_numbers():
    """sprawdza poprawnosc funkcji przy liczbie float jako argument"""
    with pytest.raises(TypeError):
        list(factorials(3.5))
