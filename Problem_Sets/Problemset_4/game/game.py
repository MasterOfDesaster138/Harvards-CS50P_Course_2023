""" 
    Title: Problemset_4 - Guessing Game

    Author: Emely Benke
    
    Created: 2023-06-02
    
    Version: 0.1
    
    Summary: 
             I’m thinking of a number between 1 and 100…

            What is it?
            It’s 50! But what if it were more random?

            In a file called game.py, implement a program that:

            Prompts the user for a level *n*, 
            . If the user does not input a positive integer, 
            the program should prompt again.
            Randomly generates an integer between 1 and *n*
            , inclusive *n* , using the random module.
            Prompts the user to guess that integer. 
            If the guess is not a positive integer, 
            the program should prompt the user again.
            If the guess is smaller than that integer, 
            the program should output Too small! and prompt the user again.
            If the guess is larger than that integer,
            the program should output Too large! and prompt the user again.
            If the guess is the same as that integer, 
            the program should output Just right! and exit.

"""
import sys, random


def main():
    # prompts a level from the user
    level = get_level()
    # selects a random number between 1 and level
    random_number = get_random_number(level)
    # prompts for a guess and checks if guess matches random_number in a loop
    while True:
        guess = prompt_guess(level)
        # checks if guess matches and returns a feedback for the user
        print(check_guess(guess, random_number))


def get_level() -> int:
    """Prompts the Level from the User and excludes negative (or other datatypes than) integers.

    Returns:
        int: returns the max level for the random number
    """
    while True:
        try: # prompting the max level of the random number
            # only accepts a positive integer
            level_input = int(input("Level: "))
            if level_input > 0:
                return level_input
            
        except:
            pass


def get_random_number(level: int) -> int:
    """Returns a random number between 1 and inclusive level argument. 

    Args:
        level (int): the inclusive maximum of the range

    Returns:
        int: a random number between 1 and inclusive level
    """
    return random.randint(1, level)


def prompt_guess(level: int) -> int:
    """Prompts a positive integer from the user to guess the random number.

    Args:
        level (int): the max possible number

    Returns:
        int: the guess of the user as integer
    """
    while True:
        try:
            guess = int(input("Guess: "))
            if 0 < guess < level+1:
                return guess
        
        except:
            pass


def check_guess(guess: int, match: int) -> str:
    """Checks if User's Guess matches the random Number and returns a feedback.
    It returns a winner message or hints if the number is larger or smaller.

    Args:
        guess (int): the inputted guess from the user
        match (int): the random number the user tries to guess

    Returns:
        str: a hint or a winning message for the user as feedback
    """
    if guess < match:
        return "Too small!"
    elif guess > match:
        return "Too large!"
    elif guess == match:
        # close the game if the user has a match
        return sys.exit("Just right!")


if __name__ == '__main__':
    main()


"""Here’s how to test your code manually:

Run your program with python game.py. 
Type cat at a prompt that says Level: and press Enter. 
Your program should reprompt you:
    Level:  
 
Run your program with python game.py. 
Type -1 at a prompt that says Level: and press Enter. 
Your program should reprompt you:
    Level:
       
Run your program with python game.py. 
Type 10 at a prompt that says Level: and press Enter. 
Your program should now be ready to accept guesses:
    Guess:
       
Run your program with python game.py.
Type 10 at a prompt that says Level: and press Enter. 
Then type cat. Your program should reprompt you:
    Guess:  
 
Run your program with python game.py. 
Type 10 at a prompt that says Level: and press Enter. 
Then type -1. Your program should reprompt you:
    Guess:
       
Run your program with python game.py. 
Type 1 at a prompt that says Level: and press Enter. 
Then type 1. Your program should output:
    Just right!  
There’s only one possible number the answer could be!

Run your program with python game.py. 
Type 10 at a prompt that says Level: and press Enter. 
Then type 100. Your program should output:
    Too large!  
Looks like you’re guessing outside the range you specified.

Run your program with python game.py. 
Type 10000 at a prompt that says Level: and press Enter. 
Then type 1. Your program should output:
    Too small!  
Most likely, anyways: you might get lucky and see Just right!. 
But it would certainly be odd for you to see Just right! every time.
And certainly you shouldn’t see Too large!.
"""

"""check50 cs50/problems/2022/python/game"""