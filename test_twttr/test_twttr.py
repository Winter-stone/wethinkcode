from twttr import shorten


def test_omission():
    assert shorten('twitter') == 'twttr'
    assert shorten('winter') == 'wntr'

def test_lowercase():
    assert shorten('TwItter') == 'Twttr'
    assert shorten('PythOn') == 'Pythn'

def test_numbers_punctuationsn():
    assert shorten('Wint3r') == 'Wnt3r'
    assert shorten('now!') == 'nw!'
    assert shorten('123456!.') == '123456!.'

