from twttr import shorten

def test_twttr1():
    assert shorten("Twitter") == "Twttr"

def test_twttr2():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_twttr3():
    assert shorten("CS50") == "CS50"

def test_twttr4():
    assert shorten("pleAse") == "pls"
