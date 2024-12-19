from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50

    with pytest.raises(ValueError):
        convert("cat/2")

    with pytest.raises(ValueError):
        convert("2/cat")

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(47) == "47%"
