import pytest
import working
from working import convert

def test_no_mins():
    assert convert('7 AM to 4 PM') == '07:00 to 16:00'
    assert convert('10 AM to 6 PM') == '10:00 to 18:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_mins():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('8:00 PM to 10:00 AM') == '20:00 to 10:00'
    assert convert('9:00 PM to 5:00 AM') == '21:00 to 05:00'

def test_errors():
    with pytest.raises(ValueError):
        convert('9 AM to 5:001 PM')

    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

    with pytest.raises(ValueError):
        convert('09:00 AM to 17:00 PM')





