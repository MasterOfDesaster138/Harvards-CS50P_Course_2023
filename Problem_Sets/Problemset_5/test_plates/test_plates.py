""" 
    Title: Problemset_5 - Re-requesting a Vanity Plate

    Author: Emely Benke
    
    Created: 2023-06-09
    
    Version: 0.1
    
    Summary:
             In a file called plates.py, reimplement Vanity Plates from Problem Set 2, 
             restructuring your code per the below, wherein is_valid still expects a str as input and 
             returns True if that str meets all requirements and False if it does not, 
             but main is only called if the value of __name__ is "__main__":

                def main():
                    ...


                def is_valid(s):
                    ...


                if __name__ == "__main__":
                    main()
                Then, in a file called test_plates.py, 
                implement four or more functions 
                that collectively test your implementation of is_valid thoroughly, 
                each of whose names should begin with test_ 
                so that you can execute your tests with:

                pytest test_plates.py
             
"""
# import the function we want to test
from plates import is_valid 


def test_two_letters():
    """Tests if the function implements the following rule:
    “All vanity plates must start with at least two letters.” """
    assert is_valid("HEY44") == True
    assert is_valid("44HEY") == False


def test_max_6_chars():
    """Tests if the function implements the following rule:
    “vanity plates may contain a maximum of 6 characters (letters or numbers).” """
    assert is_valid("HEY444") == True
    assert is_valid("HH442200") == False
    assert is_valid("HHH4422") == False


def test_numbers_not_in_middle():
    """Tests if the function implements the following rule:
    “Numbers cannot be used in the middle of a plate; they must come at the end. 
            For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
            The first number used cannot be a ‘0’.” """
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_no_special_characters():
    """Tests if the function implements the following rule:
    “No periods, spaces, or punctuation marks are allowed.” """
    assert is_valid("HEY444") == True
    assert is_valid("HEY!44") == False


def test_cs50_instructions():
    """Tests the manually tests from the problem instructions."""
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False