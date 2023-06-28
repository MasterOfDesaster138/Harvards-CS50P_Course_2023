""" 
    Title: Problemset_6 - Pizza Py

    Author: Emely Benke
    
    Created: 2023-06-27
    
    Version: 0.1
    
    Summary:
            Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, 
            known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

            Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, 
            per this CSV file of Sicilian pizzas, sicilian.csv, below:

            Sicilian Pizza,Small,Large
            Cheese,$25.50,$39.95
            1 item,$27.50,$41.95
            2 items,$29.50,$43.95
            3 items,$31.50,$45.95
            Special,$33.50,$47.95
            
            See regular.csv for a CSV file of regular pizzas as well.

            Of course, a CSV file isn’t the most customer-friendly format to look at. 
            Prettier might be a table, formatted as ASCII art, like this one:

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
            
            In a file called pizza.py, implement a program that 
            expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
            and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. 
            Format the table using the library’s grid format. 
            If the user does not specify exactly one command-line argument, 
            or if the specified file’s name does not end in .csv, 
            or if the specified file does not exist, 
            the program should instead exit via sys.exit.
"""
# Import Modules & Libraries:

import sys                      # for handling command-line arguments and exiting the program
from tabulate import tabulate   # for formatting the table
import csv                      # for reading the CSV file

##### Functions: #####

def main():
    # validates the given cl-parameter and returns the file [name or path]
    csv_file_path = validate_cl_parameter(sys.argv)
    table = generate_pizza_table(csv_file_path)
    print(table)
    quit()


def validate_cl_parameter(cl_parameter: list) -> str:
    """Validates the given command-line argument and returns the file [name or path].

    Args:
        cl_parameter (list): The list of command-line arguments.

    Returns:
        str: The validated CSV file path.

    Raises:
        SystemExit: If the number of arguments is not equal to 2 or if the specified file does not have a .csv extension.
    """
    # the user must specify exactly one command-line argument
    if len(cl_parameter) < 2:
        sys.exit("Too few command-line arguments")
    elif len(cl_parameter) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_input = cl_parameter[1].strip()
        # check if the given file is an csv file based on the file extension
        if file_input.endswith(".csv"):
            return file_input
        else:
            sys.exit("Not a CSV file")
    

def generate_pizza_table(csv_path: str) -> str:
    """
    Generates a table formatted as ASCII art using tabulate.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        str: The formatted table as a string.

    Raises:
        SystemExit: If the file does not exist or has an invalid format.
    """
    # initialize an empty list for the extracted csv data
    csv_data = []
    try:
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            header_row = next(csv_reader)
            
            # Determine the appropriate table headers based on the CSV file
            if "Sicilian Pizza" in header_row:
                table_headers = header_row[:]
            elif "Regular Pizza" in header_row:
                table_headers = header_row[:]
            else:
                raise ValueError("Invalid CSV file format")

            # Read the remaining rows and collect the data
            for row in csv_reader:
                csv_data.append(row)
                
            # Format the table using tabulate and return the formatted string
            table = tabulate(csv_data, headers=table_headers, tablefmt="grid")
            return table
        
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()


"""How to Test
Here’s how to test your code manually:

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
