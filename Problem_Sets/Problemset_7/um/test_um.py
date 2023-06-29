###### How to Test ##### 
"""Here’s how to test um.py manually:

Run your program with python um.py. 
Ensure your program prompts you for an input. 
Type um, followed by Enter. 
Your count function should return 1.

Run your program with python um.py. 
Type um?, followed by Enter. 
Your count function should return 1.

Run your program with python um.py. 
Type Um, thanks for the album., followed by Enter. 
Your count function should return 1.

Run your program with python um.py. 
Type Um, thanks, um..., followed by Enter. 
Your count function should return 2.


___How to Test test_um.py:___

To test your tests, run pytest test_um.py. 
Try to use correct and incorrect versions of um.py 
to determine how well your tests spot errors:

Ensure you have a correct version of um.py. 
Run your tests by executing pytest test_um.py. 
pytest should show that all of your tests have passed.
Modify the count function in the correct version of um.py. count might, 
for example, mistakently also count any “um” that is part of a word. 
Run your tests by executing pytest test_um.py. 
pytest should show that at least one of your tests has failed.
Again modify the count function in the correct version of um.py. 
count might, for example, mistakenly only match an “um” 
that is surrounded on either side by a space. 
Run your tests by executing pytest test_um.py. 
pytest should show that at least one of your tests has failed.
You can execute the below to check your code using check50, 
a program that CS50 will use to test your code when you submit. 
But be sure to test it yourself as well!

check50 cs50/problems/2022/python/um
Green smilies mean your program has passed a test! 
Red frownies will indicate your program output something unexpected. 
Visit the URL that check50 outputs to see the input check50 handed to your program, 
what output it expected, and what output your program actually gave."""
# import the Testframework Library
import pytest
# import the function(s) we want to test
import um 


def test_count_single_word():
    assert um.count("um") == 1
    assert um.count("Um") == 1
    assert um.count("UM") == 1
    

def test_count_sentence():
    assert um.count("Hello um, World!") == 1
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um, what do you want to eat at lunch?") == 1
    
    
def test_count_ignore_punctuation():
    assert um.count("Um, thanks, um...") == 2
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um.. um! um? um_") == 4
    
    
def test_count_ignore_similar_words():
# Collection of some similiar words 
similiar_words = ["sum", "mum", "gum", "hum", "rum", "lum", "ump", "vum", "umm", "yum"]
    # we expect that the program will ignore all words
    assert um.count(str.join(similiar_words)) == 0
    
    
