""" 
    Title: Problemset_4 - Adieu, Adieu

    Author: Emely Benke
    
    Created: 2023-06-02
    
    Version: 0.1
    
    Summary: 
        In The Sound of Music, there’s a song sung largely in English, So Long, 
        Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

        Adieu, adieu, to yieu and yieu and yieu

        Of course, the line isn’t grammatically correct, 
        since it would typically be written (with an Oxford comma) as:

        Adieu, adieu, to yieu, yieu, and yieu

        To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

        In a file called adieu.py, implement a program that prompts the user for names, 
        one per line, until the user inputs control-d. Assume that the user will input at least one name. 
        Then bid adieu to those names, separating two names with one and, 
        three names with two commas and one and, and names with 
        commas and one and, as in the below:

        Adieu, adieu, to Liesl
        Adieu, adieu, to Liesl and Friedrich
        Adieu, adieu, to Liesl, Friedrich, and Louisa
        Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
    
"""
import sys

def main():
    name_list = get_input()
    
    try:
        output = generate_output(name_list)
        print(output)
    
    except IndexError:
        sys.exit("Ups, there was a error. Try again.")

def get_input() -> list:
    """Prompts Names from the user in a Loop until he stops the input
    when he hits control-d or control-c.

    Raises:
        ValueError: don't add the input to the list 
                    and prompts again for a name after an Errormessage

    Returns:
        list: stores all inputted names in titlecase
    """
    # a list will store all inputted names of the user
    inputted_names = []
    
    # prompt the user for a name in a loop until he stops the input with control-d
    while True:
        try:
            name_input = input("Name: ").strip()
            
            if name_input.isalpha():
                inputted_names.append(name_input.title())
            else:
                raise ValueError("Invalid Input! \n You can only add Names.")
            
        except ValueError:
            pass
        
        except KeyboardInterrupt:
            if inputted_names:
                return inputted_names
            else:
                pass
            
            
            
def generate_output(names: list) -> str:
    """Generates the Output based on follwing rules.
        bid adieu to the given names, separating two names with one and, 
        three names with two commas and one and, and names with 
        commas and one and, as in the below:

        Adieu, adieu, to Liesl
        Adieu, adieu, to Liesl and Friedrich
        Adieu, adieu, to Liesl, Friedrich, and Louisa
        Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
        Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
        
    Arguments:
        names -- a list with the inputted names of the user prompting

    Returns:
        a string with the expected output
    """
    PREFIX = "Adieu, adieu, to"
    # separating two names with one and
    if len(names) == 2:
        name_suffix = f"{names[0]} and {names[1]}"
        return f"{PREFIX} {name_suffix}"   
    
    # adds the only name to the prefix
    elif len(names) == 1:
        return f"{PREFIX} {names[0]}"
    
    # separating each name with commas and an and 
    elif len(names) > 2:
        # stores the value of the last name
        last_name = names[-1]
        # prepare a string for the name_suffix_string
        name_suffix = names[0]
        
        # adds an comma between any name in the string
        for name in names:
            # exclude the last name from comma adding
            if name != last_name and name != names[0]:
                name_suffix = name_suffix + ', ' + name
                
            elif name == last_name:
                break
            
        return f"{PREFIX} {name_suffix} and {last_name}"


if __name__ == "__main__":
    main()

"""Here’s how to test your code manually:

Run your program with python adieu.py. Type Liesl and press Enter, followed by control-d. 
Your program should output:
    Adieu, adieu, to Liesl 

Run your program with python adieu.py. Type Liesl and press Enter, 
then type Friedrich and press Enter, followed by control-d. 
Your program should output:
    Adieu, adieu, to Liesl and Friedrich

Run your program with python adieu.py. Type Liesl and press Enter, 
then type Friedrich and press Enter. 
Now type Louisa and press Enter, followed by control-d. 
Your program should output:
    Adieu, adieu, to Liesl, Friedrich, and Louisa 
"""

"""check50 cs50/problems/2022/python/adieu"""

