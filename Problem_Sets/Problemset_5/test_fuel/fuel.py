"""
    Title: Problemset_3 - Fuel Gauge

    Author: Emely Benke
    
    Created: 2023-05-31
    
    Version: 0.2 -> modified for Problemset 5
    
    Summary: 
            Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
            For instance 1/4 indicates that a tank is 25% full, 
            1/2 indicates that a tank is 50% full, 
            and 3/4 indicates that a tank is 75% full.

            In a file called fuel.py, implement a program that prompts the user for a fraction, 
            formatted as X/Y, wherein each of X and Y is an integer, 
            and then outputs, as a percentage rounded to the nearest integer, 
            how much fuel is in the tank. 
            If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
            And if 99% or more remains, output F instead to indicate that the tank is essentially full.

            If, though, X or Y is not an integer, 
            X is greater than Y, or Y is 0, 
            instead prompt the user again. 
            (It is not necessary for Y to be 4.) 
            Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
def main():
    # prompt a fraction from user
    fractions = get_input()
    # convert the fractions into an percentage value
    percentage = convert(fractions)
    # print the output for the user
    print(gauge(percentage))


def get_input():
    """ Prompts a Fraction from user.
        Formatted as X/Y, wherein each of X and Y is an integer."""
    while True:
        fraction_input = input("Fraction: ").strip()
        try:
            # separate the numbers for validating
            fraction_1, fraction_2 = fraction_input.split('/')
            if validate_fractions(fraction_1, fraction_2):
                return (int(fraction_1), int(fraction_2))
            
        except ValueError:
            pass


def validate_fractions(fraction_1: str, fraction_2: str) -> bool:
    """ Validate the inputted fraction
        If, though, X or Y is not an integer, 
        X is greater than Y, or Y is 0, 
        instead prompt the user again"""
    try:
        # convert strings to integers
        x, y = int(fraction_1), int(fraction_2)
        # check fraction validation
        if x <= y and y != 0:
            return True
        else:
            raise ValueError

    except ValueError:
        return False


def convert(fractions: tuple) -> int:
    """ Converts and outputs the fraction,
        as a percentage rounded to the nearest integer."""
    fuel_percentage = fractions[0] / fractions[1] * 100
    return int(round(fuel_percentage, 0))


def gauge(fuel_percentage: int) -> str:
    """ Generate the Fuel Output for the user.
        If, though, 1% or less remains, output E instead 
        to indicate that the tank is essentially empty. 
        And if 99% or more remains, output F instead 
        to indicate that the tank is essentially full."""
    if fuel_percentage <= 1:
        return "E"
    elif fuel_percentage >= 99:
        return "F"
    else:
        return f"{fuel_percentage}%"


if __name__ == '__main__':
    main()


""""Here’s how to test your code manually:

Run your program with python fuel.py. Type 3/4 and press Enter. 
Your program should output:
    75%
     
Run your program with python fuel.py. Type 1/4 and press Enter. 
Your program should output:
    25%
    
Run your program with python fuel.py. Type 4/4 and press Enter. 
Your program should output:
    F
    
Run your program with python fuel.py. Type 0/4 and press Enter. 
Your program should output:
    E
    
Run your program with python fuel.py. Type 4/0 and press Enter. 
Your program should handle a ZeroDivisionError and prompt the user again.

Run your program with python fuel.py. Type three/four and press Enter. 
Your program should handle a ValueError and prompt the user again.

Run your program with python fuel.py. Type 1.5/3 and press Enter. 
Your program should handle a ValueError and prompt the user again.

Run your program with python fuel.py. Type 5/4 and press Enter. 
Your program should prompt the user again."""

"""check50 cs50/problems/2022/python/fuel"""