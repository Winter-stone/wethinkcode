import pytest
import seasons
from seasons import season

def test_seasons():
    assert season('1999-01-01') == 'Thirteen million, nine hundred eighty-nine thousand, six hundred minutes'
    assert season("2001-01-01") == 'Twelve million, nine hundred thirty-six thousand, nine hundred sixty minutes'
    assert season("2020-06-01") == 'Two million, seven hundred twenty-five thousand, nine hundred twenty minutes'

