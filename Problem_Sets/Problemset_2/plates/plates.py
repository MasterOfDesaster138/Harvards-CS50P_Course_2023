"""
   Title: Problemset_1 - Vanity Plates

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1
    
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
    plate_input  = input("Type in a Plate: ")
    print(is_valid(plate_input))
    


def is_valid(plate: str) -> str:
    """Validate the Plate request based on given rules.
    
         “All vanity plates must start with at least two letters.”
        “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        “Numbers cannot be used in the middle of a plate; they must come at the end. 
            For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
            The first number used cannot be a ‘0’.”
        “No periods, spaces, or punctuation marks are allowed.”
    """   
    if 6 < len(plate) < 2:                                              # holds min. 2 & max. 6 characters
        return 'Invalid'                               
        if not plate[0].isalpha() and not plate[1].isalpha():           # starts with min. 2 letters
            return 'Invalid'                                                
        
            for char in plate:
                if char in ('.', ' ', '!'):                             # if not a alpanumeric charater was found return False
                    return 'Invalid'
                if char.isdigit() and plate[-1].isalpha():              # if plate contains numbers i cannot ends with letters
                    return 'Invalid'
        
    if plate[0] == '0':                                                 # cannot start with a '0'
        return 'Invalid'

    return 'Valid'



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