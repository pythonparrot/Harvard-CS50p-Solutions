import pytest

from seasons import convert

def test_seasons1():
    assert convert("2023-12-26") == "Five hundred twenty-seven thousand forty minutes"

def test_seasons2():
    assert convert("2022-12-26") == "One million, fifty-two thousand, six hundred forty minutes"

def test_seasons3():
    with pytest.raises(SystemExit):
        convert("January 1, 2001")

