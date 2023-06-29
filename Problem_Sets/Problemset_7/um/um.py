""" 
    Title: Problemset_7 - Regular, um, Expressions

    Author: Emely Benke
    
    Created: 2023-06-28
    
    Version: 0.1
    
    Summary:
            It’s not uncommon, in English, at least, to say “um” 
            when trying to, um, think of a word. The more you do it, 
            though, the more noticeable it tends to be!

            In a file called um.py, implement a function called count 
            that expects a line of text as input as a str and returns, 
            as an int, the number of times that “um” appears in that text, 
            case-insensitively, as a word unto itself, 
            not as a substring of some other word. 
            For instance, given text like hello, um, world, 
            the function should return 1. 
            Given text like yummy, though, the function should return 0.

            Structure um.py as follows, wherein you’re welcome to modify main and/or 
            implement other functions as you see fit, but you may not import any other libraries. 
            You’re welcome, but not required, to use re and/or sys.
                
            Either before or after you implement count in um.py, additionally implement, 
            in a file called test_um.py, three or more functions that collectively test 
            your implementation of count thoroughly, each of whose names should begin 
            with test_ so that you can execute your tests with:

            --> pytest test_um.py
"""
"""Hints
Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including findall.

Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.

Because backslashes in regular expressions could be mistaken for escape sequences (like \n), 
best to use Python’s raw string notation for regular expression patterns. 
Just as format strings are prefixed with f, so are raw strings prefixed with r. 
For instance, instead of "harvard\.edu", use r"harvard\.edu".

Note that \b is “defined as the boundary between a \w and a \W character (or vice versa), 
or between \w at the beginning/end of the string,” 
per docs.python.org/3/library/re.html#regular-expression-syntax.

You might find regex101.com or regexr.com 
helpful for testing regular expressions (and visualizing matches).
See thefreedictionary.com/words-containing-um for some words that contain “um”."""

# Imports:
import re
import sys


# Functions: 
def main():
    print(count(input("Text: ")))


def count(input_text: str) -> int:
    """The function expects a line of text as input as a str 
    and returns, as an int, the number of times that “um” appears in that text, 
    case-insensitively, as a word unto itself, not as a substring of some other word. """
    re_pattern = re.compile(r"\bum\b", re.I)
    
    # scan the whole text for all pattern matches
    re_matches = re.findall(re_pattern, input_text) 

    # return the total number of matches for the inputted text
    return len(re_matches)


# Main program flow
if __name__ == "__main__":
    main()
    
    
"""Here’s how to test um.py manually:

Run your program with python um.py. Ensure your program prompts you for an input. 
Type um, followed by Enter. Your count function should return 1.

Run your program with python um.py. Type um?, followed by Enter. 
Your count function should return 1.

Run your program with python um.py. Type Um, thanks for the album., 
followed by Enter. Your count function should return 1.

Run your program with python um.py. Type Um, thanks, um..., followed by Enter. 
Your count function should return 2."""