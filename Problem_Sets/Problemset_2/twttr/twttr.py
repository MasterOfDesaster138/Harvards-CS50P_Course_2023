"""
   Title: Problemset_1 - Just setting up my twttr

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1
    
    Summary: 
        When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
        much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts 
        the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
        whether inputted in uppercase or lowercase.
"""
def main():
    text_input = input("Type in your Message: ")
    
    VOWELS = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
    for char in VOWELS:
        text_input = text_input.replace(char,'')

    print(text_input)

if __name__ == '__main__':
    main()
    
    

"""Here’s how to test your code manually:

Run your program with python twttr.py. Type Twitter and press Enter. 
Your program should output:
    Twttr
       
Run your program with python twttr.py. Type What's your name? and press Enter. 
Your program should output:
    Wht's yr nm?
    
Run your program with python twttr.py. Type CS50 and press Enter. 
Your program should output:
    CS50
"""


"""check50 cs50/problems/2022/python/twttr"""