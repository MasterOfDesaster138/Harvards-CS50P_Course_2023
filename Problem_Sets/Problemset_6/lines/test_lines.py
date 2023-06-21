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