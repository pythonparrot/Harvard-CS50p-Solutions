from fuel import convert
import pytest

def test_convert():
    assert convert("1/2") == "50%"

    with pytest.raises(ValueError):
        convert("cat/2") == "50%"
