import pytest
from jar import Jar

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_erroes():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

    with pytest.raises(ValueError):
        jar.withdraw(1)
