"""
    Title: Problemset_3 - Emojize

    Author: Emely Benke
    
    Created: 2023-06-01
    
    Version: 0.1
    
    Summary: 
        Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, 
        some programs support “codes,” whereby you can type, for instance, 
        :thumbs_up:, which will be automatically converted to 👍. 
        Some programs additionally support aliases, whereby you can more succinctly type, 
        for instance, :thumbsup:, which will also be automatically converted to 👍.

        See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

        In a file called emojize.py, implement a program 
        that prompts the user for a str in English 
        and then outputs the “emojized” version of that str, 
        converting any codes (or aliases) therein to their corresponding emoji.
"""
# import e third party library 
import emoji

def main():
    # promts the user and validates the input
    user_input = get_input()
    # translates the inputted string and prints it to the user
    print(f"Output: {emoji.emojize(user_input, language='alias')}")


def get_input() -> str:
    """ Prompts the User for a string that can
        contain any emoji aliases or codes.

    Returns:
        str: the inputted string
    """
    while True:
        try:
            # prompts the user
            return input("Input: ").strip()

        except ValueError:  # catches Errors at the input
            pass


if __name__ == '__main__':
    main()
    

""""Here’s how to test your code manually:

Run your program with python emojize.py. Type :1st_place_medal: and press Enter. 
Your program should output:
    Output: 🥇

Run your program with python emojize.py. Type :money_bag: and press Enter. 
Your program should output:
    Output: 💰

Run your program with python emojize.py. Type :smile_cat: and press Enter. 
Your program should output:
    Output: 😸
"""

"""check50 cs50/problems/2022/python/emojize"""