"""
    Title: Problemset_0 - Tip Calculator

    Author: Emely Benke
    
    Created: 2023-05-26
    
    Version: 0.1
    
    Summary:
            Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

            dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
            => remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
            percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
            => remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
            
            Assume that the user will input values in the expected formats.
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """Removes the leading $, and returns the amount as a float.

    Args:
        d (str): formatted as $##.##, wherein each # is a decimal digit

    Returns:
        float:  amount as a float
    """
    return float(d.removeprefix('$'))


def percent_to_float(p: str) -> float:
    """remove the trailing %, and return the percentage as a float.

    Args:
        p (str): formatted as ##%, wherein each # is a decimal digit

    Returns:
        float: the percentage as a float
    """
    percentage = float(p.removesuffix('%'))
    return percentage / 100
    

if __name__ == '__main__':
    main()