##### How to Test: #####

""" How to Test seasons.py:

Here’s how to test seasons.py manually:

Run your program with python seasons.py. Ensure your program prompts you for a birthdate. 
Type a date one year ago from today, in the specified format, then press Enter.
Your program should sing print Five hundred twenty-five thousand, six hundred minutes.

Run your program with python seasons.py. Type a date two years ago from today, 
in the specified format, then press Enter. 
Your program should print One million, fifty-one thousand, two hundred minutes.

Run your program with python seasons.py. Type a date of your choice, 
but this time use an invalid format. Press Enter and your program 
should exit using sys.exit without raising an Exception.
"""

""" How to Test test_seasons.py:

To test your tests, run pytest test_seasons.py. 
Try to use correct and incorrect versions of seasons.py 
to determine how well your tests spot errors:

Ensure you have a correct version of seasons.py. 
Run your tests by executing pytest test_seasons.py. 
pytest should show that all of your tests have passed.

Modify one of the functions you’ve implemented in seasons.py 
and imported into test_seasons.py. One of your functions might, 
for example, fail to raise a ValueError when it should. 
Run your tests by executing pytest test_seasons.py. 
pytest should show that at least one of your tests has failed.

Continue to modify the behavior of seasons.py, 
creating (predictably) incorrect versions of your implementation. 
Run your tests by executing pytest test_seasons.py. 
Do the tests you expect to fail, fail?
"""
import pytest

from seasons import convert_minutes_to_words, get_date


def test_convert_minutes_to_words_one_year():
    assert convert_minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    

def test_convert_minutes_to_words_two_years():
    assert convert_minutes_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
    
    
def test_get_date_invalid_date():
    with pytest.raises(SystemExit) as execinfo:
        get_date("   ")