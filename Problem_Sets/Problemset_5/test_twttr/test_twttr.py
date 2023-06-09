""" 
   Title: Problemset_5 - Testing my twttr

    Author: Emely Benke
    
    Created: 2023-06-07
    
    Version: 0.1
    
    Summary:
            In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, 
            restructuring your code per the below, wherein shorten expects a str as input 
            and returns that same str but with all vowels (A, E, I, O, and U) omitted, 
            whether inputted in uppercase or lowercase.

            def main():
                ...


            def shorten(word):
                ...


            if __name__ == "__main__":
                main()
                
                
            Then, in a file called test_twttr.py, implement one or more functions 
            that collectively test your implementation of shorten thoroughly, 
            each of whose names should begin with test_ so that you can execute your tests with:

            pytest test_twttr.py 
    
"""

# import the function we want to test
from twttr import shorten


def test_shorten_uppercase_word():
    """Tests if it removes uppercase vowel letters in the word."""
    assert shorten("HELLO") == "HLL"


def test_shorten_lowercase_word():
    """Tests if it removes lowercase vowel letters in the word."""
    assert shorten("great") == "grt"


def test_shorten_sentence():
    """Tests if it removes vowels in all words of a sentence."""
    assert shorten("How are you?") == "Hw r y?" 


def test_shorten_numbers():
    """Tests if numbers remain untreated."""
    assert shorten("2023") == "2023"


def test_shorten_no_vowels():
    """Tests if an input without vowels remains unhandled."""
    assert shorten("crypt") == "crypt"
    

def test_from_instructions():
    """Tests the manually test instructions from the original Problemset."""
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"