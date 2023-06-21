""" 
    Title: Problemset_5 - Refueling

    Author: Emely Benke
    
    Created: 2023-06-11
    
    Version: 0.1
    
    Summary:
             In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, 
             restructuring your code per the below, wherein:

                convert expects a str in X/Y format as input, 
                wherein each of X and Y is an integer, 
                and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. 
                If X and/or Y is not an integer, or if X is greater than Y, 
                then convert should raise a ValueError. If Y is 0, 
                then convert should raise a ZeroDivisionError.
                gauge expects an int and returns a str that is:
                "E" if that int is less than or equal to 1,
                "F" if that int is greater than or equal to 99,
                and "Z%" otherwise, wherein Z is that same int.
                
                def main():
                    ...


                def convert(fraction):
                    ...


                def gauge(percentage):
                    ...


                if __name__ == "__main__":
                    main()
                Then, in a file called test_fuel.py, 
                implement two or more functions that collectively test your implementations 
                of convert and gauge thoroughly, each of whose names should begin with test_ 
                so that you can execute your tests with:

                --> pytest test_fuel.py
"""
# import the functions we want to test
from fuel import convert, gauge, validate_fractions

# Testcases for the Convert function
def test_convert_rounding():
    """Tests if the function converts the inputted fraction to the proper rounded percentage. """
    assert convert((3, 4)) == 75
    assert convert((1, 4)) == 25
    assert convert((2, 5)) == 40


# Testcases for the Validation Function
def test_validate_fractions_exceptions():
    """Tests if the function handles exceptions like given requirements from instructions."""
    assert validate_fractions("4", "0") == False
    assert validate_fractions("three", "four") == False
    assert validate_fractions("1.5", "3") == False
    assert validate_fractions("5", "4") == False


# Testcases for the Gauge function
def test_gauge_symbols():
    """Tests if the function outputs F or E, when the tank is full or empty."""
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    """Tests if the function outputs the proper percentage as string."""
    assert gauge(25) == "25%"
    assert gauge(33) == "33%"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"