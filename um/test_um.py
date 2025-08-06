import pytest
import um
from um import count

def test_count():
    assert count('hello, my name is um, Marvin, umbrella in my um car yummy') == 2
    assert count('hello, um, my name um is um, Marvin, umbrella in my um car.') == 4
    assert count('I am eating this yummy snack, under my umbrella') == 0

def test_characters():
    assert count('hello, my name is um. Marvin, umbrella in my um? car') == 2
    assert count('hello, my name is (um), Marvin, umbrella in my !um>? car yummy') == 2

def test_case_sensitivity():
    assert count('hello, my name is UM, Marvin, umbrella in my Um car') == 2
    assert count('So UM, from today on foward, I am uM the UN president') == 2
