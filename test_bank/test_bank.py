import bank
from bank import value

def test_values():
    assert value('hello') != 20
    assert value('Hey, hello') != 100

def test_not_hello():
    assert value('hey') == 20
    assert value('Hey, there') == 20
    assert value('HY, how are you') == 20

def test_not_h():
    assert value('Whats up?') == 100
    assert value('Are you alright?') == 100
