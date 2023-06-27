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
        ["lines.py", "loc2.py"]
        ],
    
    'any_files': [
        ["lines.py", "loc.txt"],
        ["lines.py", "loc.sql"]
        ],
    
    'too_few_args':  ["lines.py"], 
    
    'too_many_args': [
        ["lines.py", "lines.py", "--V"],
        ["lines.py", "loc1.py", "--V", "helloworld.cpp"]
    ],
    
    'file_not_exists': [
        ["lines.py", "suka.py"],
        ["lines.py", "aloha.py"]
    ],
    
    'filepaths': [
        # this files does exists
        ["lines.py", r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\tests\filepathtest.py"], 
        ["lines.py", r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\tests\loc_path.py"]
    ], 
    
    'metric_cornercases': ["lines.py", r"C:\Users\emely\Documents\GitHub\Harvards-CS50P_Course\Problem_Sets\Problemset_6\tests\metric_cornercase.py"]
}


##### Testcases for validate_arguments() #####

def test_validate_arguments_toofew(capfd):
    """Tests if the function 'validate_arguments' accepts exactly one command-line argument."""
    # Setup the simulated command line arguments for testing
    fake_argv = TEST_DOUBLES["too_few_args"]

    # Test how the function handles too few command line arguments
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(fake_argv)

        # Check if 'sys.exit' was called
        assert exit_info.type == SystemExit

        # Get the output message of the standard error output stream
        captured = capfd.readouterr()
        error_message = captured.err.strip()

        # Compare captured error message with the expected error message from the requirements
        expected_error_msg = "Too few command-line arguments"
        assert error_message == expected_error_msg


def test_validate_arguments_toomany1(capfd):
    """Tests if the function 'validate_arguments' accepts excactly one command-line argument."""
    # setup the simulated cl-arguments for testing
    case1_argv = TEST_DOUBLES["too_many_args"][0]
    
    # tests how the function handles too many command line arguments
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(case1_argv)
    
        # checks if 'sys.exit' was called   
        assert exit_info.type == SystemExit
        
        # get the outputmessage of the standard error output stream
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        
        # compares catched error message with the expected error message from the requirements
        expected_error_msg = "Too many command-line arguments"
        assert error_message == expected_error_msg
    
  
def test_validate_arguments_toomany2(capfd):    
    """Tests if the function 'validate_arguments' accepts excactly one command-line argument."""
    case2_argv = TEST_DOUBLES["too_many_args"][1]
    
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(case2_argv)  
        
        assert exit_info.type == SystemExit
        
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        
        expected_error_msg = "Too many command-line arguments"
        assert error_message == expected_error_msg


def test_validate_arguments_pythonfile_valid():
    """Tests if the function 'validate_arguments' accepts only python files."""
    # setup simulated command line arguments for proper testing of validate_arguments()
    python_file1, python_file2 = TEST_DOUBLES["python_files"]
    
    # files with the extension '.py' should be valid
    assert validate_arguments(python_file1) == True
    assert validate_arguments(python_file2) == True
    
    
def test_validate_arguments_pythonfile_invalid(capfd):
    """Tests if the function 'validate_arguments' accepts only python files."""
    # setup simulated command line arguments for proper testing of validate_arguments()
    any_file1, any_file2 = TEST_DOUBLES['any_files']
    expected_error_msg = "Not a Python file"
    
    # Testcase 1: 'loc.txt'
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(any_file1)
        
        assert exit_info.type == SystemExit
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        assert error_message == expected_error_msg
    
    # Testcase 2: 'loc.sql'
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(any_file1)
        
        assert exit_info.type == SystemExit
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        assert error_message == expected_error_msg


##### Testcases for file_handling() #####

def test_file_handling_filepath_not_exists(capfd):
    """Tests if the function 'file_handling' proper handles exceptions, if file cannot be found."""
    # setup simulated command line arguments for proper testing of validate_arguments()
    pseudo_filepath1, pseudo_filepath2 = TEST_DOUBLES["file_not_exists"]
    expected_error_msg = "File does not exist"  # as required in instructions
    
    # Testcase 1: 'suka.py'
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(pseudo_filepath1[1])
        
        assert exit_info.type == SystemExit
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        assert error_message == expected_error_msg
    
    # Testcase 2: 'aloha.py'
    with pytest.raises(SystemExit) as exit_info:
        validate_arguments(pseudo_filepath2[1])
    
        assert exit_info.type == SystemExit
        captured = capfd.readouterr()
        error_message = captured.err.strip()
        assert error_message == expected_error_msg


def test_file_handling_filepath_exists():
    """Tests if the function 'file_handling' can handle filepaths instead of filenames."""
    # setup simulated command line arguments for proper testing of validate_arguments()
    filepath1 = TEST_DOUBLES["filepaths"][0][1]
    filepath2 = TEST_DOUBLES["filepaths"][1][1]
    
    assert file_handling(filepath1) == {'LOC': 22, 'SLOC': 14, 'CLOC': 1, 'BLOC': 7}
    assert file_handling(filepath2) == {'LOC': 9, 'SLOC': 5, 'CLOC': 1, 'BLOC': 3}
    

def test_file_handling_metric_counter():
    """Tests if the function 'file_handling' determines the expected LOC-KPI for the given file."""
    # setup simulated command line arguments for proper testing of validate_arguments()
    python_file1, python_file2 = TEST_DOUBLES["python_files"]
    
    # Testcase 1: 'loc1.py'
    assert file_handling(python_file1[1]) == {'LOC': 22, 'SLOC': 14, 'CLOC': 1, 'BLOC': 7}
    
    
    # Testcase 2: 'loc2.py'
    assert file_handling(python_file2[1]) == {'LOC': 3, 'SLOC': 2, 'CLOC': 1, 'BLOC': 0}
    
    
def test_file_handling_metric_cornercase():
    # setup simulated command line arguments for proper testing of validate_arguments()
    file_path = TEST_DOUBLES['metric_cornercases'][1]
    
    # python file only contains blank lines and comments
    expected_metrics = {'LOC': 8, 'SLOC': 0, 'CLOC': 4, 'BLOC': 4}
    assert file_handling(file_path) == expected_metrics
