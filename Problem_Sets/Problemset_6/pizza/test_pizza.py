##### How to Test #####
"""Here’s how to test your code manually:

Run your program with python pizza.py. Your program should exit using sys.exit and 
provide an error message: Too few command-line arguments

Be sure to download regular.csv and sicilian.csv, placing them in the same folder as pizza.py. 
Run your program with python pizza.py regular.csv sicilian.csv. 
Your program should output: Too many command-line arguments

Run your program with python pizza.py invalid_file.csv. 
Assuming invalid_file.csv doesn’t exist, your program should exit using sys.exit and 
provide an error message: File does not exist

Create a file named sicilian.txt. 
Run your program with python pizza.py sicilian.txt. Your program should exit using sys.exit and 
provide an error message: Not a CSV file

Run your program with python pizza.py regular.csv. 
Assuming you’ve downloaded regular.csv, 
your program should print a table like the below:
+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+


You can execute the below to check your code using check50, 
a program that CS50 will use to test your code when you submit. 
But be sure to test it yourself as well!

--> check50 cs50/problems/2022/python/pizza
Green smilies mean your program has passed a test! 
Red frownies will indicate your program output something unexpected. 
Visit the URL that check50 outputs to see the input check50 handed to your program, 
what output it expected, and what output your program actually gave."""

##### INSTRUCTIONS: #####
""" In a file called pizza.py, implement a program that 
    expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
    and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. 
    Format the table using the library’s grid format. 
    If the user does not specify exactly one command-line argument, 
    or if the specified file’s name does not end in .csv, 
    or if the specified file does not exist, 
    the program should instead exit via sys.exit."""
    
# import the functions we want to test from pizza.py 
from pizza import validate_cl_parameter, generate_pizza_table 
import pytest


# simulate required data for proper functions testing 
TEST_DATA = {
    
}


##### Testcases for validate_cl_paramter() #####

def test_validate_cl_parameters_quantity_few():
    """Tests if the program exits with the correct errormessage, if there are too few cl parameters inputted."""
    expected_error_message = "Too few command-line arguments"
    pass


def test_validate_cl_parameters_quantity_many():
    """Tests if the program exits with the correct errormessage, if there are too many cl parameters inputted."""
    expected_error_message = "Too many command-line arguments"
    pass


def test_validate_cl_parameters_file_extensions_valid():
    """Tests if the functions returns excepted value, if the inputted cl-parameter is valid."""
    pass


def test_validate_cl_parameters_file_extensions_invalid():
    """Tests if the program exits with the correct errormessage, if the inputted file is not an CSV."""
    expected_error_message = "Not a CSV file"
    pass


def test_validate_cl_parameters_file_not_exists():
    """Tests if the program exits with the correct errormessage, if the file doesn't exists."""
    expected_error_message = "File does not exist"
    pass


def test_validate_cl_parameters_file_exists():
    """Tests if the function returns the expected value, if the file does exists."""
    pass



##### Testcases for generate_pizza_table() #####

def test_generate_pizza_table():
    """Test if the function returns a string, that matches the given data, and is formatted as ascii table in the 'grid' style."""
    pass