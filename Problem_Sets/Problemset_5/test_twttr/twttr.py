"""
   Title: Problemset_1 - Just setting up my twttr

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.2 (modified for Problemset 5)
    
    Summary: 
        When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
        much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts 
        the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
        whether inputted in uppercase or lowercase.
"""
def main():
    text_input = input("Type in your Message: ")
    print(shorten(text_input))
    
def shorten(word: str) -> str:
    # tuple with all Vowels in upper and lower case
    VOWELS = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
    # loop through all Vowels and replace them in the inputted word
    for char in VOWELS:
        word = word.replace(char,'')
    # return the new word without vowels 
    return word

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