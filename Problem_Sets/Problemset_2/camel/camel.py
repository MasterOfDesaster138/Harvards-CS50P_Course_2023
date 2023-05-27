"""
   Title: Problemset_1 - camelCase

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1
    
    Summary: 
        In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names 
        when those names comprise multiple words, whereby the first letter of the first word is lowercase but 
        the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, 
        a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) 
        might be called preferredFirstName.

        Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. 
        For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

        In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and 
        outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
"""
def main():
    camel_case = input("Type a camelCase Variable: ").strip()
    snake_case = camel_to_snake(camel_case)
    print(snake_case)
            
            
def camel_to_snake(camel_case: str) -> str:
    # separate each Word with an '_'
    snake_case = ''
    for character in camel_case:
        if character.isupper():
            snake_case += '_' + character.lower()
        else:
            snake_case += character
    return snake_case


if __name__ == '__main__':
    main()



"""Here’s how to test your code manually:

Run your program with python camel.py. Type name and press Enter. 
Your program should output:
    name
   
Run your program with python camel.py. Type firstName and press Enter. 
Your program should output:
    first_name

Run your program with python camel.py. Type preferredFirstName and press Enter. 
Your program should output:
    preferred_first_name
"""


"""check50 cs50/problems/2022/python/camel"""