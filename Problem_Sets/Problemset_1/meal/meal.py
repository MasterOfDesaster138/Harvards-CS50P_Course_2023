"""
   Title: Problemset_1 - Meal Time

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1
    
    Summary: 
        Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
        lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. 
        Wouldn’t it be nice if you had a program that could tell you what to eat when?

        In meal.py, implement a program that prompts the user for a time and outputs 
        whether it’s breakfast time, lunch time, or dinner time. 
        If it’s not time for a meal, don’t output anything at all. 
        Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
        And assume that each meal’s time range is inclusive. 
        For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

        Structure your program per the below, 
        wherein convert is a function (that can be called by main) that converts time, 
        a str in 24-hour format, to the corresponding number of hours as a float. 
        For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours)
        
    Challenge:
        If up for a challenge, optionally add support for 12-hour times, 
        allowing the user to input times in these formats too:
            #:## a.m. and ##:## a.m.
            #:## p.m. and ##:## p.m.
"""

def main():
    time_input = input("Type in a time: ")
    formatted_time = convert(time_input)
    current_mealtime(formatted_time)


def convert(time: str) -> float:
    """Converts a Time-String (24H Format) to the corresponding number of hours as a float (Decimal Time Format)."""
    # unpack the values from user input
    hours, minutes = time.split(':')
    
    # convert the variables from string to int
    hours = int(hours)
    minutes = int(minutes)
    
    # convert minutes to decimal time format
    minutes_dec = minutes / 60
    # add decimal-formatted minutes to hours
    formatted_time = float(hours) + minutes_dec
    
    return formatted_time


def current_mealtime(time: float) -> str:
    """Checks if given time is a mealtime, and returns current meal based on it

    Args:
        time (float): time in decimal format [HH.MM]

    Returns:
        str: title of current meal based on given time or noting if no match.
    """
    if 7.00 <= time <= 8.00:
        return print("breakfast time")
    
    elif 12.00 <= time <= 13.00:
        return print("lunch time")
    
    elif 18.00 <= time <= 19.00:
        return print("dinner time")



if __name__ == "__main__":
    main()
    
    

"""Here’s how to test your code manually:

Run your program with python meal.py. Type 7:00 and press Enter. 
Your program should output:
    breakfast time   

Run your program with python meal.py. Type 7:30 and press Enter. 
Your program should output:
    breakfast time

Run your program with python meal.py. Type 12:42 and press Enter. 
Your program should output:
    lunch time

Run your program with python meal.py. Type 18:32 and press Enter. 
Your program should output:
    dinner time

Run your program with python meal.py. Type 11:11 and press Enter. 
Your program should output: 
    nothing
"""


"""check50 cs50/problems/2022/python/meal"""