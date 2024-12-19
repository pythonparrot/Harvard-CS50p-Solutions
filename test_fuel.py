from fuel import convert
import pytest

def test_convert():
    assert convert("1/2") == "50%"

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
