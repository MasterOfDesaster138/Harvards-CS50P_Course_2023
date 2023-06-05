""" 
    Title: Problemset_4 - Figlet

    Author: Emely Benke
    
    Created: 2023-06-01
    
    Version: 0.1
    
    Summary: 
            FIGlet, named after Frank, Ian, and Glen’s letters, is a program 
            from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

            _ _ _          _   _     _
            | (_) | _____  | |_| |__ (_)___
            | | | |/ / _ \ | __| '_ \| / __|
            | | |   <  __/ | |_| | | | \__ \
            |_|_|_|\_\___|  \__|_| |_|_|___/
            Among the fonts supported by FIGlet are those at figlet.org/examples.html.

            FIGlet has since been ported to Python as a module called pyfiglet.

            In a file called figlet.py, implement a program that:

            Expects zero or two command-line arguments:
            Zero if the user would like to output text in a random font.
            Two if the user would like to output text in a specific font, 
            in which case the first of the two should be -f or --font, 
            and the second of the two should be the name of the font.
            Prompts the user for a str of text.
            Outputs that text in the desired font.
            If the user provides two command-line arguments 
            and the first is not -f or --font 
            or the second is not the name of a font, 
            the program should exit via sys.exit with an error message.
"""
import sys, random

from pyfiglet import Figlet

# setup a figlet instance to use the library
figlet = Figlet()


# create a list that contains all avaible fonts for figlet
FONT_LIST = figlet.getFonts()

def main():
    # program excepts 0 or 2 command line arguments
    if len(sys.argv) in (1, 2, 3):
        # promts a string from the user
        text_input = input("Input: ")
        
        # handles 3 arguments and validates them before executing
        if len(sys.argv) == 3 and validate_cl_arguments():
            # outputs the figlet to the user
            print(f"{generate_figlet(sys.argv[2], text_input)}")
            
        elif len(sys.argv) == 2 and validate_cl_arguments():
            # iterate through all possible fonts and prints out the given text
            iter_all_fonts(text_input) # no return value from function
            
        elif validate_cl_arguments:
            # select a random font from the list of avaible fonts from figlet
            random_font = random.choice(FONT_LIST)
            # outputs the figlet to the user
            print(f"{generate_figlet(random_font, text_input)}")
          
    # handles an unexpected number on arguments or invalid arguments
    else:
        sys.exit("Expects zero or two command-line arguments: \n"
                	"-> Zero if the user would like to output text in a random font. \n"
                    "-> Two if the user would like to output text in a specific font, \n" 
                        	"in which case the first of the two should be -f or --font, \n" 
                            "and the second of the two should be the name of the font. \n")


def validate_cl_arguments() -> bool:
    """If the user provides two command-line arguments 
            and the first is not -f or --font 
            or the second is not the name of a font, 
            the program should exit via sys.exit with an error message."""
    if sys.argv[1] in ('-f', '--font') and sys.argv[2] in FONT_LIST:
        return True
    elif sys.argv[1] in ('-a', '--all'):
        return True
    else:
        return False


def generate_figlet(font: str, text: str) -> str: 
    """Generates a figlet of inputted str with given font."""
    # set selected font for the figlet object
    figlet.setFont(font=font)
    
    # generate figlet for the user of inputted text
    return figlet.renderText(text)

def iter_all_fonts(text: str):
    """Iterate through all possible Fonts and print the Text out."""
    for font in FONT_LIST:
        print(f"{font}:")
        print(f"{generate_figlet(font, text)}")
    

if __name__ == '__main__':
    main()
    
    

"""Here’s how to test your code manually:

Run your program with python figlet.py test. 
Your program should exit via sys.exit and print an error message:
    Invalid usage

Run your program with python figlet.py -a slant. 
Your program should exit via sys.exit and print an error message:
    Invalid usage

Run your program with python figlet.py -f invalid_font. 
Your program should exit via sys.exit and print an error message:
    Invalid usage

Run your program with python figlet.py -f slant. Type CS50. 
Your program should print the following:
   ___________ __________ 
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ / 
\____//____/_____/\____/  


Run your program with python figlet.py -f rectangles. Type Hello, world. 
Your program should print the following:
 _____     _ _                        _   _ 
|  |  |___| | |___      _ _ _ ___ ___| |_| |
|     | -_| | | . |_   | | | | . |  _| | . |
|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|                       
                  
                  
Run your program with python figlet.py -f alphabet. Type Moo. 
Your program should print the following:

M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo  
                   
"""

"""check50 cs50/problems/2022/python/figlet"""