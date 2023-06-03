""" 
    Title: Problemset_4 - Little Professor

    Author: Emely Benke
    
    Created: 2023-06-02
    
    Version: 0.1
    
    Summary: 
             One of David’s first toys as a child, funny enough, 
             was Little Professor, a “calculator” that would 
             generate ten different math problems for David to solve. 
             For instance, if the toy were to display 4 + 0 = , 
             David would (hopefully) answer with 4. 
             If the toy were to display 4 + 1 = , 
             David would (hopefully) answer with 5. 
             If David were to answer incorrectly, the toy would display EEE. 
             And after three incorrect answers for the same problem, 
             the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

            In a file called professor.py, implement a program that:

            Prompts the user for a level, *n*. 
            If the user does not input 1, 2, or 3, 
            the program should prompt again.
            Randomly generates ten (10) math problems formatted as X + Y = , 
            wherein each of X and Y is a non-negative integer with *n* digits. 
            No need to support operations other than addition (+).
            Prompts the user to solve each of those problems. 
            If an answer is not correct (or not even a number), 
            the program should output EEE and prompt the user again, 
            allowing the user up to three tries in total for that problem. 
            If the user has still not answered correctly after three tries, 
            the program should output the correct answer.
            The program should ultimately output the user’s score: 
            the number of correct answers out of 10.
            Structure your program as follows, wherein get_level prompts 
            (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
            and generate_integer returns a randomly generated non-negative integer 
            with level digits or raises a ValueError if level is not 1, 2, or 3:
    
"""
import random


def main():
    # init game settings
    score = 0
    # prompts the level from the user
    level = get_level()
    # creates 10 random math problems for that specific level
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y}"
        answer = x + y
        # the user has 3 chances to solve the problem
        for _ in range(3):
            if solve_problem(problem, answer):
                score += 1
                break
            # print an error respond if the user don't matches the correct answer
            else: 
                print("EEE")
                
        # If the user has still not answered correctly after three tries
        else:
            print(f"The correct answer is: {answer}")
            
    # print the score to the user at the end.
    print (f"Your Score is {score}/10!")


def get_level() -> int:
    """Prompts a level from the user and reprompts if this level don't exists.

    Returns:
        int: the selected level of the user
    """
    while True:
        try:
            level = (input("Level: "))
            if level in ('1', '2', '3'):
                return int(level)
            else:
                raise ValueError("Invalid Level! Must be 1, 2, or 3.")
     
        except ValueError:
            pass


def generate_integer(level: int) -> int:
    """Returns a randomly generated non-negative integer with the specified number of digits."""
    min_value = 10 ** (level - 1)
    max_value = (10 ** level) - 1
    return random.randint(min_value, max_value)


def solve_problem(problem: str, answer: int) -> bool:
    """Solves a math problem and returns True if the answer is correct, False otherwise."""
    answer_input = input(f"{problem} = ")
    try:
        if int(answer_input) == answer:
            return True
        else:
            raise ValueError
        
    except ValueError:
        return False


if __name__ == "__main__":
    main()
    
    
""" Here’s how to test your code manually:

Run your program with python professor.py. Type -1 and press Enter. 
Your program should reprompt you:
    Level:
       
Run your program with python professor.py. Type 4 and press Enter. 
Your program should reprompt you:
Level:   

Run your program with python professor.py. Type 1 and press Enter. 
Your program should begin posing addition problems with positive, single-digit integers. 
    For example: 6 + 6 =    
Your program should output 10 distinct problems 
before printing the number of questions you answered correctly and exiting.

Run your program with python professor.py. Type 1 and press Enter. 
Answer the first question incorrectly. Your program should output:
    EEE
before reprompting you with the same question.

Run your program with python professor.py. Type 1 and press Enter. 
Answer the first question incorrectly, three times. 
Your program should output the correct answer. 
    For example: 6 + 6 = 12
and then move on to another question. 
Answer the remaining questions correctly. 
Your program should output a score of 9.

Run your program with python professor.py. Type 1 and press Enter. 
Answer all 10 questions correctly. Your program should output a score of 10.
"""

"""check50 cs50/problems/2022/python/professor"""