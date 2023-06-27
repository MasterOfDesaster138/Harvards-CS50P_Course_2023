""" 
Here’s how to test your code manually:

Run your program with python lines.py. Your program should exit with sys.exit and provide an error message:
Too few command-line arguments

Create two python programs, hello.py and goodbye.py. Run python lines.py hello.py goodbye.py. Your program should exit with sys.exit and provide an error message:
Too many command-line arguments

Create a text file called invalid_extension.txt. Run your program with python lines.py invalid_extension.txt. Your program should exit with sys.exit and provide an error message:
Not a Python file

Run your program with python lines.py non_existent_file.py. Assuming non_existent_file.py doesn’t exist, your program should exit with sys.exit and provide an error message:
File does not exist

Create additional python programs which vary in complexity:
create some with comments, some docstrings, and some whitespace. 
For each of these files run python lines.py FILENAME where FILENAME is the name of the file. 
lines.py should output the number of lines, excluding comments and whitespace, present in the given file.

"""
# import the functions we want to test
from lines import validate_arguments, file_handling
import pytest, sys


# define simulated values for sys.argv[1] to test the functions
TEST_DOUBLES = {
    'python_files': [
        ["lines.py", "loc1.py"],
        ["lines.py", "loc2.py"],
        ["lines.py", "loc3.py"]
        ],
    
    'any_files': [
        ["lines.py", "loc.txt"],
        ["lines.py", "loc.sql"],
        ["lines.py", "loc.java"],
        ],
    
    'to_few_args':  ["lines.py"], 
    
    'to_many_args': [
        ["lines.py", "lines.py", "--V"],
        ["lines.py", "loc1.py", "--V", "helloworld.cpp"]
    ],
    
    'file_not_exists': [
        # this files don't exists
        ["lines.py", "suka.py"],
        ["lines.py", "aloha.py"],
        
        # this files does exists
        ["lines.py", "C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\tests\filepathtest.py"], 
        ["lines.py", "C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\tests\loc_path.py"]
    ]
}


# Testcases for validate_arguments()
def test_validate_arguments_quantity():
    """Tests if the function 'validate_arguments' accepts excactly one command-line argument."""
    assert validate_arguments()


def test_validate_arguments_pythonfile():
    """Tests if the function 'validate_arguments' accepts only python files."""
    pass


# Testcases for file_handling()
def test_file_handling_filepath():
    """Tests if the function 'file_handling' proper handles exceptions, if file cannot be found."""
    pass


def test_file_handling_metric_counter():
    """Tests if the function 'file_handling' determines the expected LOC-KPI for the given file."""
    pass
