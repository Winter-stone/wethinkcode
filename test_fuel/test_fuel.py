import fuel
import pytest
from fuel import convert, gauge

def test_values():
    assert convert('1/2') == 50
    assert convert('1/100') == 1
    assert convert('1/1') == 100

def test_percentage():
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

    with pytest.raises(ValueError):
        convert('-1/2')
