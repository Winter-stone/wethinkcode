import pytest
import numb3rs
from  numb3rs import validate

def test_valid_address():
    assert validate('1.2.3.4') == True
    assert validate('255.255.255.255') == True
    assert validate('197.0.0.1') == True

def test_leading_zero():
    assert validate('127.0.001.1') == False
    assert validate('255.252.197.01') == False
    assert validate('0.0001.1.1') ==  False

def test_errors():
    assert validate('cat.bat.dog.rat') == False
    assert validate('1.0.0.dog') == False