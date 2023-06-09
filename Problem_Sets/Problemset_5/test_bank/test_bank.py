""" 
    Title: Problemset_5 - Back to the Bank

    Author: Emely Benke
    
    Created: 2023-06-09
    
    Version: 0.1
    
    Summary:
             In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, 
             restructuring your code per the below, wherein value expects a str as input and 
             returns 0 if that str starts with “hello”, 
             20 if that str starts with an “h” (but not “hello”), 
             or 100 otherwise, treating the str case-insensitively. 
             You can assume that the string passed to the value function will not contain any leading spaces. 
             Only main should call print.

                def main():
                    ...


                def value(greeting):
                    ...


                if __name__ == "__main__":
                    main()
                Then, in a file called test_bank.py, 
                implement three or more functions that collectively test your implementation of value thoroughly, 
                each of whose names should begin with test_ so that you can execute your tests with:

                pytest test_bank.py
    
"""
# import the function we want to test
from bank import value


def test_value_0():
    """Tests if the function returns '$0' if the greeting starts with 'hello' [case-insensitively]."""
    assert value("hello") == "$0"
    assert value("hello, David") == "$0"
    assert value("Hello") == "$0"
    assert value("HELLO") == "$0"


def test_value_20():
    """Tests if the function returns '$20' if the greeting starts with the letter 'h' [case-insensitively]."""
    assert value("hi") == "$20"
    assert value("hola") == "$20"
    assert value("Hi, David") == "$20"
    assert value("Hey") == "$20"
    assert value("HI") == "$20"


def test_value_100():
    """Tests if the function returns '$100' if the greeting doesn't starts with 'h' or matches 'hello' [case-insensitively]."""
    assert value("privjet") == "$100"
    assert value("Bonjour") == "$100"
    assert value("Aloha, David") == "$100"
    assert value("KONICHIWA") == "$100"


def test_value_from_instructions():
    """Tests the manually tests from the instructions of the original Problemset."""
    assert value("Hello") == "$0"
    assert value("Hello, Newman") == "$0"
    assert value("How you doing?") == "$20"
    assert value("What's happening?") == "$100"