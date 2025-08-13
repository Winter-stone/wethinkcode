import cows_and_bulls
from cows_and_bulls import no_duplicates, get_player_secret

def test_duplicates():
    assert no_duplicates('1234') == None
    assert no_duplicates('1231') == 'dups'

def test_player():
    assert get_player_secret('1234') == '1234'
    assert get_player_secret('1231') == None

def test_zero():
    assert get_player_secret('1234') == '1234'
    assert get_player_secret('1230') == None