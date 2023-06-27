""" 
    Title: Problemset_6 - Lines of Code

    Author: Emely Benke
    
    Created: 2023-06-21
    
    Version: 0.1
    
    Summary:
             One way to measure the complexity of a program is to count its number of lines of code (LOC),
             excluding blank lines and comments. For instance, a program like

            # Say hello
            name = input("What's your name? ")
            print(f"hello, {name}")
            
            has just two lines of code, not four, since its first line is a comment,
            and its second line is blank (i.e., just whitespace). 
            That’s not that many, so odds are the program isn’t that complex. 
            Of course, just because a program (or even function) has more lines of code 
            than another doesn’t necessarily mean it’s more complex. For instance, a function like

            def is_even(n):
                if n % 2 == 0:
                    return True
                else:
                    return False
                    
            isn’t really twice as complex as a function like

            def is_even(n):
                return n % 2 == 0
                
            even though the former has (more than) twice as many lines of code. 
            In fact, the former might arguably be simpler if it’s easier to read! 
            So lines of code should be taken with a grain of salt.

            Even so, in a file called lines.py, implement a program that 
            expects exactly one command-line argument, the name (or path) of a Python file, 
            and outputs the number of lines of code in that file, excluding comments and blank lines. 
            If the user does not specify exactly one command-line argument,
            or if the specified file’s name does not end in .py, or if the specified file does not exist, 
            the program should instead exit via sys.exit.

            Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
            (A docstring should not be considered a comment.) 
            Assume that any line that only contains whitespace is blank.
    
"""
# Import Modules and Libraries
import sys


# Functions:
def main():
    # if the given argument is valid, compute LOC-Metric of the given file
    if validate_arguments(sys.argv):
        file_stats = file_handling(sys.argv[1])

    if file_stats:
        # Output the total of Source Code Lines of the given file
        print(f"{file_stats['SLOC']}")
        quit()


def validate_arguments(cl_args) -> bool:
    """Validates the command-line arguments.
    Only one argument, a python file name, is accepted."""
    # the program excepts only one command line argument
    if len(cl_args) == 1 :
        sys.exit("Too few command-line arguments")
    elif len(cl_args) > 2:
        sys.exit("Too many command-line arguments")    
    else:
        # only python files will be accepted
        if not cl_args[1].endswith(".py"):
            sys.exit("Not a Python file")
        else:
            return True


def file_handling(file_path: str) -> dict:
    """Handles the File object, inclusive exceptions.
    Iterates through the file and counts the "LOC Statistics"."""
    # A dict to store the computed values
    file_stats = {
    'LOC': 0,               # Total of all lines, inclusive comments and blanks
    'SLOC': 0,              # Total of lines, exclusice comments and blanks
    'CLOC': 0,              # Total of lines, that contains comments
    'BLOC': 0               # Total of lines, that are blank / holds only whitespace
}
    
    try: # tries to open file from FileDescriptorOrPath String extracted from commmand-line argument
        with open(file_path, 'r') as file: # opens file in read mode 
            
            # iterate through each line from the open file
            for line in file: 
                file_stats['LOC'] += 1 # increase LOC_Stat, no matter what the line contains
                # first remove leading and trailing whitespace before the line will be analyzed
                line = line.strip()
                # check for a blank line 
                if not line:
                    file_stats['BLOC'] += 1
                # check if line contains only a comment
                elif line.startswith('#'):
                    file_stats['CLOC'] += 1
                # we assume that every other line content contains either source code or docstrings
                else:
                    file_stats['SLOC'] += 1
              
        # returns file_stats dictionary if no error occurs       
        return file_stats    
        
    # Catch error, if file or path cannot be found
    except FileNotFoundError:
        sys.exit("File does not exist")
        


if __name__ == '__main__':
    main()
    


"""Here’s how to test your code manually:

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
You can execute the below to check your code using check50, 
a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!
===> check50 cs50/problems/2022/python/lines
Green smilies mean your program has passed a test! 
Red frownies will indicate your program output something unexpected. 
Visit the URL that check50 outputs to see the input check50 handed to your program,
what output it expected, and what output your program actually gave."""