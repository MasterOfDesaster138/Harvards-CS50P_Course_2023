"""
    Title: Problemset_1 - Deep Thought

    Author: Emely Benke
    
    Created: 2023-05-26
    
    Version: 0.1
    
    Summary:
            “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
            “You’re really not going to like it,” observed Deep Thought.
            “Tell us!”
            “All right,” said Deep Thought. “The Answer to the Great Question…”
            “Yes…!”
            “Of Life, the Universe and Everything…” said Deep Thought.
            “Yes…!”
            “Is…” said Deep Thought, and paused.
            “Yes…!”
            “Is…”
            “Yes…!!!…?”
            “Forty-two,” said Deep Thought, with infinite majesty and calm.”
                                                                            — The Hitchhiker’s Guide to the Galaxy, Douglas Adams

            In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
            the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
            Otherwise output No.
"""

def main():
    # Prepare a tuple with all valid answers for the following question
    VALID_ANSWERS = ('42', 'forty-two', 'forty two')
    
    # ask the user the most important question
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything?: ").lower()
    
    # check if answer of the user matches any of the valid options
    if user_input.strip() in VALID_ANSWERS:
        return print('Yes')
    else:    
        return print('No')
    

if __name__ == '__main__':
    main()
    
    
    
    
"""Here’s how to test your code manually:

Run your program with python deep.py. Type 42 and press Enter. 
Your program should output:
    Yes
     
Run your program with python deep.py. Type Forty Two and press Enter. 
Your program should output:
    Yes

Run your program with python deep.py. Type forty-two and press Enter. 
Your program should output:
    Yes

Run your program with python deep.py. Type 50 and press Enter. 
Your program should output:
    No

Be sure to vary the casing of your input and 
“accidentally” add spaces on either side of your input before pressing enter. 
Your program should behave as expected, case- and space-insensitively."""


"""check50 cs50/problems/2022/python/deep"""