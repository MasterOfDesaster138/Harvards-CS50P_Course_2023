"""
   Title: Problemset_1 - Coke Machine

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1
    
    Summary: 
            The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that 
            “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. 
            Retail stores are welcome to download the posters, print, display and/or distribute them to consumers 
            in close proximity to the relevant foods in the stores.”

            In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) 
            and then outputs the number of calories in one portion of that fruit,
            per the FDA’s poster for fruits, which is also available as text. 
            Capitalization aside, assume that users will input fruits exactly as written in the poster 
            (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
"""
def main():
    # prompt a fruit from user
    fruit_input = user_input_handling()
    
    # search inputted fruit in FDA-Dataset
    fruit_info = match_fruit(fruit_input)
    
    # Output formatted Fruit-Infos


def user_input_handling() -> str:
    pass


def match_fruit(fruit:str) -> str:
    pass


if __name__ == '__main__':
    main()


"""Here’s how to test your code manually:

Run your program with python nutrition.py. Type Apple and press Enter. 
Your program should output:
    Calories: 130   

Run your program with python nutrition.py. Type Avocado and press Enter. 
Your program should output:
    Calories: 50

Run your program with python nutrition.py. Type Sweet Cherries and press Enter. 
Your program should output
    Calories: 100

Run your program with python nutrition.py. Type Tomato and press Enter. 
Your program should output nothing.
Be sure to try other fruits and vary the casing of your input. 
Your program should behave as expected, case-insensitively."""



"""check50 cs50/problems/2022/python/nutrition"""