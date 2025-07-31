import plates
from plates import is_valid

def test_begin_aplha():
    assert is_valid('22') == False
    assert is_valid('RW235') == True
    assert is_valid('35PO') == False

def test_alpha_first_num_last():
    assert is_valid('ERT8') == True
    assert is_valid('76RT') == False
    assert is_valid('ER76Y') == False

def test_char_length():
    assert is_valid('EE') == True
    assert is_valid('WRE532') == True
    assert is_valid('E') == False
    assert is_valid('WWERT66') == False

def test_placement():
    assert is_valid("SRT07") == False
    assert is_valid("SD#@5") == False
    assert is_valid('WRT897') == True
