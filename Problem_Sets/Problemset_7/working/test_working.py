""" _________How to Test working.py________
Here’s how to test working.py manually:

Run your program with python working.py. 
Ensure your program prompts you for a time. 
Type 9 AM to 5 PM, followed by Enter. 
Your program should output 09:00 to 17:00.

Run your program with python working.py. 
Type 9:00 AM to 5:00 PM, followed by Enter. 
Your program should again output 09:00 to 17:00.

Run your program with python working.py. 
Ensure your program prompts you for a time. 
Type 10 PM to 8 AM, followed by Enter. 
Your program should output 22:00 to 08:00.

Run your program with python working.py. 
Ensure your program prompts you for a time. 
Type 10:30 PM to 8:50 AM, followed by Enter. 
Your program should again output 22:30 to 08:50.

Run your program with python working.py. 
Ensure your program prompts you for a time. 
Try intentionally inducing a ValueError by 
typing 9:60 AM to 5:60 PM, followed by Enter. 
Your program should indeed raise a ValueError.

Run your program with python working.py. 
Ensure your program prompts you for a time. 
Try intentionally inducing a ValueError 
by typing 9 AM - 5 PM, followed by Enter. 
Your program should indeed raise a ValueError.

Run your program with python working.py. 
Ensure your program prompts you for a time. 
Try intentionally inducing a ValueError 
by typing 09:00 AM - 17:00 PM, followed by Enter. 
Your program should indeed raise a ValueError.


__________How to Test test_working.py________

To test your tests, run pytest test_working.py. 
Try to use correct and incorrect versions of working.py 
to determine how well your tests spot errors:

Ensure you have a correct version of working.py. Run your tests by executing pytest test_working.py. 
pytest should show that all of your tests have passed.
Modify the correct version of working.py, particularly its function convert. 
Your program might, for example, fail to raise a ValueError when it should. 
Run your tests by executing pytest test_working.py. 
pytest should show that at least one of your tests has failed.
Similarly, modify the correct version of working.py, 
changing the return values of convert. 
Your program might, for example, mistakenly omit minutes. 
Run your tests by executing pytest test_working.py. 
pytest should show that at least one of your tests has failed.

You can execute the below to check your code using check50, 
a program that CS50 will use to test your code when you submit. 
But be sure to test it yourself as well!

check50 cs50/problems/2022/python/working
"""
import pytest 
from working import convert


def test_convert_9am_to_5pm():
    # test the converting with single hour time formats
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    # test also the convert function with hour and minutes
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    

def test_convert_10pm_to_8am():
    # test the converting with single hour time formats
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    # test also the convert function with hour and minutes
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    
    
def test_convert_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM") 
        

def test_convert_invalid_separator_hour_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        
        
def test_convert_invalid_separator_hours_minutes():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
     
        
def  test_convert_without_abbreviation():
    with pytest.raises(ValueError):
        convert("09:00 to 12:00")