import pytest
from seasons import convert

def test_seasons1():
    assert convert("2023-12-26") == "Five hundred twenty-seven thousand forty minutes"
