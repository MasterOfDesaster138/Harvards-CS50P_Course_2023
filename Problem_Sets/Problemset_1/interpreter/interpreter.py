"""
   Title: Problemset_1 - Math Interpreter

    Author: Emely Benke
    
    Created: 2023-05-26
    
    Version: 0.1
    
    Summary: 
        Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. 
        But let’s write a program that enables users to do math, even without knowing Python.

        In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and 
        then calculates and outputs the result as a floating-point value formatted to one decimal place. 
        Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, 
        wherein:
            -> x is an integer
            -> y is +, -, *, or /
            -> z is an integer
        
        For instance, if the user inputs 
            --> 1 + 1, 
        your program should output 
            --> 2.0. 
            
        Assume that, if y is /, then z will not be 0.

        Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
"""

def main():
    # prompting for user input 
    formula = input("Type an arithmetic expression: ").strip() # unpack the inputted string
    
    # converts the operands to integers
    x, y, z = formula.split()
    x = int(x)
    z = int(z)
    
    # Print Result for Output
    print(calc_expression(x, y, z))
    
    
def calc_expression(x: int, y: str, z: int) -> float:
    """calculates the given arithmetic expression.

    Args:
        x (int): first operand
        y (str): operator ( +, -, *, or / )
        z (int): second operand

    Returns:
        float: result as a floating-point value formatted to one decimal place
    """
    match y:
        case '+':           # add
            result = x + z
            
        case '-':           # substract
            result = x - z
            
        case '*':           # multiply
            result = x * z
            
        case '/':           # divide
            result = x / z
            
        case _:             # catch Value Error
            raise ValueError("Invalid Operator.")
        
    # output floating-point value formatted to one decimal place
    return round(float(result), 1)


if __name__ == '__main__':
    main()




"""Here’s how to test your code manually:

Run your program with python interpreter.py. Type 1 + 1 and press Enter. 
Your program should output:
    2.0
     
Run your program with python interpreter.py. Type 2 - 3 and press Enter. 
Your program should output:
    -1.0

Run your program with python interpreter.py. Type 2 * 2 and press Enter. 
Your program should output:
    4.0

Run your program with python interpreter.py. Type 50 / 5 and press Enter. 
Your program should output:
    10.0
"""



"""check50 cs50/problems/2022/python/interpreter"""