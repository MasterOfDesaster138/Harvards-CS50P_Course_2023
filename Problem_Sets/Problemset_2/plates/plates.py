"""
   Title: Problemset_1 - Vanity Plates

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.2
    
    Summary: 
        In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, 
        with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

        “All vanity plates must start with at least two letters.”
        “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        “Numbers cannot be used in the middle of a plate; they must come at the end. 
            For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
            The first number used cannot be a ‘0’.”
        “No periods, spaces, or punctuation marks are allowed.”
        
        In plates.py, implement a program that prompts the user for a vanity plate and 
        then output Valid if meets all of the requirements or Invalid if it does not. 
        Assume that any letters in the user’s input will be uppercase. Structure your program per the below, 
        wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
        You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
        """
        
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    """Validate the Plate request based on given rules.
    
         “All vanity plates must start with at least two letters.”
        “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        “Numbers cannot be used in the middle of a plate; they must come at the end. 
            For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
            The first number used cannot be a ‘0’.”
        “No periods, spaces, or punctuation marks are allowed.”
    """ 
    special_characters = (' ', ',', '.', '?', '!', '-', '_', ';', ':', '=', '/', '\\', '#', '+',
                          '*', '§', '$', '%', '&', '(', ')', '[', ']', '{'', }', '@', '<', '>')
    
    # minimum is 2 and maximum 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    
    # must start with at least two letters
    if not s[0:2].isalpha():
        return False
    
    # loop through each character of the string
    for char in s:
        # only letters and numbers valid
        if char in special_characters:
            return False
 
    # loop through each character of the string    
    for char in s:
        # the first used number cannot be a 0
        if char.isnumeric():
            if char == '0' or s[-1].isalpha(): # if there are numbers used, then the plate cannot end with an letter
                return False
            # loop through each character from the first occurence of a number
            pos = s.index(char)
            for c in s[pos:]:
                # after used numbers, there are no alpha characters allowed
                if c.isalpha():
                    return False
            else:
                break
    
    # if all conditions passed, the string seems valid      
    return True  
    


if __name__ == '__main__':
    main()
    
    

"""Here’s how to test your code manually:

Run your program with python plates.py. Type CS50 and press Enter. 
Your program should output:
    Valid
    
Run your program with python plates.py. Type CS05 and press Enter. 
Your program should output:
    Invalid
    
Run your program with python plates.py. Type CS50P and press Enter. 
Your program should output:
    Invalid

Run your program with python plates.py. Type PI3.14 and press Enter. 
Your program should output:
    Invalid

Run your program with python plates.py. Type H and press Enter.
Your program should output:
    Invalid

Run your program with python plates.py. Type OUTATIME and press Enter. 
Your program should output:
    Invalid
"""


"""check50 cs50/problems/2022/python/plates"""