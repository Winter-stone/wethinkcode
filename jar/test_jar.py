import pytest
from jar import Jar

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_errors():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

    with pytest.raises(ValueError):
        jar.withdraw(1)

    with pytest.raises(ValueError):
        jar.capacity = -1

def test_deposit():
    jar = Jar()
    assert jar.deposit(12) == 12

def test_withdraw():
    jar = Jar()
    assert jar.deposit(12) == 12
    assert jar.withdraw(10) == 2

def test_init():
    jar = Jar()
    assert jar.capacity == 12
