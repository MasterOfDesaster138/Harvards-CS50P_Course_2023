##### How to Test #####
"""Here’s how to test your code manually:

Run your program with python scourgify.py. Your program should exit using sys.exit 
and provide an error message: Too few command-line arguments

Create empty files 1.csv, 2.csv, and 3.csv. Run your program with python scourgify.py 1.csv 2.csv 3.csv. 
Your program should output: Too many command-line arguments

Run your program with python scourgify.py invalid_file.csv output.csv. 
Assuming invalid_file.csv doesn’t exist, your program should exit using sys.exit 
and provide an error message: Could not read invalid_file.csv

Run your program with python scourgify.py before.csv after.csv. 
Assuming before.csv exists, your program should create a new file, 
after.csv, whose columns should be, in order, first, last, and house.


You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. 
But be sure to test it yourself as well!

--> check50 cs50/problems/2022/python/scourgify
Green smilies mean your program has passed a test! 
Red frownies will indicate your program output something unexpected. 
Visit the URL that check50 outputs to see the input check50 handed to your program, 
what output it expected, and what output your program actually gave."""
# import the functions we want to test 
from scourgify import validate_user_input, input_file_reader, tranformate_data_schema, output_file_writer

import pytest, os 

# setup required data for testing the functions
TEST_DATA = {
    # General Data 
    'INPUT_FILE': "before.csv",
    'OUTPUT_FILE': "after.csv",
    'ERROR_MSG_1': "Too few command-line arguments",
    'ERROR_MSG_2': "Too many command-line arguments",
    'ERROR_MSG_3': "Could not read ", 
    'INPUT_SCHEMA': ('name', 'house'),
    'OUTPUT_SCHEMA': ('firstname', 'lastname', 'house'),
    
    # Prepared argumentslists-Sets for the specific testcases
    'TOO_FEW_ARGS': ["scourgify.py", "before.csv"],
    
    'TOO_MANY_ARGS': [
        ["scourgify.py", "before.csv", "after.csv", "-append"],
        ["scourgify.py", "before.csv", "after.csv", "--a", "C:\Users\documents"]
    ],
    
    'FILE_NOT_FOUND_ARGS': ["scourgify.py", "invalid_file.csv", "after.csv"],
    
    'VALID_ARGS': ["scourgify.py", "before.csv", "after.csv"]
}



##### Testcases for validate_user_input(): #####

def test_validate_user_input_qty_few_args(capfd):
    # retrieve the test data from a prepared collection 
    cl_params = TEST_DATA['TOO_FEW_ARGS']
    expected_error_message = TEST_DATA['ERROR_MSG_1']
    
    # Testing how the function handles too few cl-parameters
    with pytest.raises(SystemExit) as run_info:
        validate_user_input(cl_params)
        # Check if 'sys.exit' was called
        assert run_info.type == SystemExit
        # Get the output message of the standard output stream
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        # Compare captured error message with the expected error message from the requirements
        assert error_message == expected_error_message


def test_validate_user_input_qty_many_args(capfd):
    # retrieve the test data from a prepared collection 
    cl_params1 = TEST_DATA['TOO_MANY_ARGS'][0]
    cl_params2 = TEST_DATA['TOO_MANY_ARGS'][1]
    expected_error_message = TEST_DATA['ERROR_MSG_2']
    
# Testcase 1:
    # Testing how the function handles too few cl-parameters
    with pytest.raises(SystemExit) as run_info:
        validate_user_input(cl_params1)
        # Check if 'sys.exit' was called
        assert run_info.type == SystemExit
        # Get the output message of the standard output stream
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        # Compare captured error message with the expected error message from the requirements
        assert error_message == expected_error_message

# Testcase 2:
    # Testing how the function handles too few cl-parameters
    with pytest.raises(SystemExit) as run_info:
        validate_user_input(cl_params)
        # Check if 'sys.exit' was called
        assert run_info.type == SystemExit
        # Get the output message of the standard output stream
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        # Compare captured error message with the expected error message from the requirements
        assert error_message == expected_error_message


def test_validate_user_input_valid():
    cl_params = TEST_DATA['VALID_ARGS']
    assert validate_user_input(cl_params) == True
    
    

##### Testcases for input_file_reader(): #####

def test_input_file_reader_file_not_found(capfd):
    # retrieve the test data from a prepared collection
    cl_params = "invalid_file.csv"
    expected_error_message = TEST_DATA['ERROR_MSG_3']
    
    # Testing how the function handles too few cl-parameters
    with pytest.raises(SystemExit) as run_info:
        input_file_reader(cl_params)
        # Check if 'sys.exit' was called
        assert run_info.type == SystemExit
        # Get the output message of the standard output stream
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        # Compare captured error message with the expected error message from the requirements
        assert error_message == expected_error_message
    

def test_input_file_reader_valid_file():
    # Defines temporary the path to a valid test file 
    input_file = "valid_file.csv"
    
    # Creates a Example-CSV-File with valid data
    with open(input_file, "w") as file:
        file.write("name,house\n")
        file.write('"Abbott, Hannah",Hufflepuff\n')
        file.write('"Bell, Katie",Gryffindor\n')
        file.write('"Bones, Susan",Hufflepuff\n')
        
    # Call the function we want to test
    csv_data = input_file_reader(input_file)
    
    # Checks if the result matches expected Output
    expected_data = [
        {"name": "Abbott, Hannah", "house": "Hufflepuff"},
        {"name": "Bell, Katie", "house": "Gryffindor"},
        {"name": "Bones, Susan", "house": "Hufflepuff"}
    ]
    assert csv_data == expected_data
    
    # Delete the test file after finished Test Run
    os.remove(input_file)
    
    
def test_input_file_reader_empty_file():
    # Defines a path for a temporary File for this testcase 
    empty_file = 'empty_file.csv'
    
    # create an empty file for function testing
    with open(empty_file, "x") as file:
        pass 
    
    # check if the functioncall returns an blank datacollection as expected
    assert input_file_reader(empty_file) == []
    
    # Removes the test file after finished test run
    os.remove(empty_file)
    
    
def test_input_file_reader_without_columns():
    # Defines a filepath for this testcase
    invalid_file = "no_header.csv"
    
    # Creates a Example-CSV-File without header
    with open(invalid_file, "w") as file:
        file.write('"Abbott, Hannah",Hufflepuff\n')
        file.write('"Bell, Katie",Gryffindor\n')
        file.write('"Bones, Susan",Hufflepuff\n')
        
    # Call the function that we want to test
    csv_data = input_file_reader(invalid_file)
    
    # Checks if the result matches expected Output
    expected_data = []
    assert csv_data == expected_data
    
    # Delete the test file after finished Test Run
    os.remove(input_file)
    
    
def test_input_file_reader_incorrect_csv_format():
    # Defines a filepath of a temporary file for this testcase
    incorrect_format_file = "missing_csv_format.csv"
    
    # Creates a Example-CSV-File without an correct CSV-File-Format
    with open(incorrect_format_file, "w") as file:
        file.write("name,house\n")
        file.write('"Harry Potter"\n')
        file.write('"Bell, Katie",Gryffindor\n')
        file.write('"Bones, Susan",Hufflepuff\n')
        
    # Catches a csv.Error if the function was called with an unformatted csv file
     with pytest.raises(csv.Error):
        input_file_reader(incorrect_format_file)
    
    # Removes the temp file after the test run finished   
    os.remove(incorrect_format_file)
    
    
    
##### Testcases for tranformate_data_schema() #####

def test_tranformate_data_schema():
    input_data = [
        {"name": "Abbott, Hannah", "house": "Hufflepuff"},
        {"name": "Bell, Katie", "house": "Gryffindor"},
        {"name": "Creevey, Colin", "house": "Gryffindor"}
    ]
    expected_output = [
        {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
        {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
        {"first": "Colin", "last": "Creevey", "house": "Gryffindor"}
    ]
    assert tranformate_data_schema(input_data) == expected_output
    
    
def test_tranformate_data_schema_empty_input():
    input_data = []
    expected_output = []
    assert tranformate_data_schema(input_data) == expected_output
    
    
def test_tranformate_data_schema_single_row():
    input_data = [{"name": "Smith, John", "house": "Ravenclaw"}]
    expected_output = [{"first": "John", "last": "Smith", "house": "Ravenclaw"}]
    assert tranformate_data_schema(input_data) == expected_output


##### Testcases for output_file_writer(): #####

def test_output_file_writer(tmp_path):
    output_file = tmp_path / "output.csv"
    datacollection = [
        {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
        {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
        {"first": "Colin", "last": "Creevey", "house": "Gryffindor"}
    ]
    expected_output = [
        "firstname,lastname,house\n",
        "Hannah,Abbott,Hufflepuff\n",
        "Katie,Bell,Gryffindor\n",
        "Colin,Creevey,Gryffindor\n"
    ]
    output_file_writer(datacollection, output_file)
    with open(output_file, "r") as file:
        assert file.readlines() == expected_output


def test_output_file_writer_empty_data(tmp_path):
    output_file = tmp_path / "output.csv"
    datacollection = []
    expected_output = ["firstname,lastname,house\n"]
    output_file_writer(datacollection, output_file)
    with open(output_file, "r") as file:
        assert file.readlines() == expected_output


def test_output_file_writer_existing_file(tmp_path):
    output_file = tmp_path / "existing.csv"
    # Create an existing file
    with open(output_file, "w") as file:
        file.write("existing data")
    datacollection = [
        {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
        {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
        {"first": "Colin", "last": "Creevey", "house": "Gryffindor"}
    ]
    expected_output = [
        "firstname,lastname,house\n",
        "Hannah,Abbott,Hufflepuff\n",
        "Katie,Bell,Gryffindor\n",
        "Colin,Creevey,Gryffindor\n"
    ]
    output_file_writer(datacollection, output_file)
    with open(output_file, "r") as file:
        assert file.readlines() == expected_output


def test_output_file_writer_file_permissions(tmp_path):
    output_file = tmp_path / "output.csv"
    datacollection = [
        {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
        {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
        {"first": "Colin", "last": "Creevey", "house": "Gryffindor"}
    ]
    output_file_writer(datacollection, output_file)
    file_permissions = os.stat(output_file).st_mode & 0o777
    assert file_permissions == 0o666
