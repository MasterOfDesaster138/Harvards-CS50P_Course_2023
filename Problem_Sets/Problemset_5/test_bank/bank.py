"""
   Title: Problemset_1 - Home Federal Savings Bank

    Author: Emely Benke
    
    Created: 2023-05-26
    
    Version: 0.2 (modified for Problemset 5)
    
    Summary: 
        In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone 
        who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” 
        and so he asks for $100. The bank’s manager proposes a compromise: 
        “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

        In a file called bank.py, implement a program that prompts the user for a greeting. 
        If the greeting starts with “hello”, output $0. 
        If the greeting starts with an “h” (but not “hello”), output $20. 
        Otherwise, output $100. 
        
        Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
"""
def main():
    # prompt for users greeting 
    greeting = input("Type a greeting: ")
    greeting = greeting.lstrip() # remove any leading whitespace
    # outputs the greeting to the user
    print(value(greeting))
    
    
def value(greeting: str) -> str:    
    greeting = greeting.lower() # converts input to lowercase string
    # Controlflow for output based on given greeting
    if greeting.startswith('hello'):
        return '$0'
    elif greeting.startswith('h'):
        return '$20'
    else:
        return '$100'
    
    
if __name__ == '__main__':
    main()
    
    
    

"""Here’s how to test your code manually:

Run your program with python bank.py. Type Hello and press Enter. 
Your program should output:
    $0
     
Run your program with python bank.py. Type Hello, Newman and press Enter. 
Your program should output:
    $0
    
Run your program with python bank.py. Type How you doing? and press Enter. 
Your program should output:
    $20

Run your program with python bank.py. Type What's happening? and press Enter. 
Your program should output:
    $100
"""



"""check50 cs50/problems/2022/python/bank"""