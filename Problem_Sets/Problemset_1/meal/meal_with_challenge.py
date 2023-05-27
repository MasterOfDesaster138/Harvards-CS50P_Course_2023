"""
   Title: Problemset_1 - Meal Time

    Author: Emely Benke
    
    Created: 2023-05-26
    
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
    # prompt for a time value 
    time = input("Type in a time: ")
    
    time_24 = time_to_24H_format(time)
    
    formatted_time = convert(time_24)
    current_mealtime(formatted_time)


def time_to_24H_format(time: str) -> str:
    """determine the given timeformat (12 or 24 Hours) and return the given time [in 24H Format].

    Args:
        time (str): time value given as a string

    Returns:
        list: returns a list containing hours and minutes unpacked
    """
       
    # Translates 12H Format to 24H Format Hour ['12H': "24H"]
    P_M_CONVERTER = {   '12': "12", '01': "13", '02': "14", '03': "15", '04': "16", '04': "16", '04': "16", 
                        '05': "17", '06': "18", '07': "19", '08': "20", '09': "21", '10': "22",  '11': "23" }
                                      
    
    # checks if the time is given in 12 Hours Format
    if len(time.split()) == 2:
        # unpack values from time string
        hours, rest = time.split(':')
        minutes, period = rest.split()
        
        # converts hours based on given period
        if period == 'a.m.' and hours == '12': # catch the exception at midnight
            hour = '00'
            return f"{hour}:{minutes}"
        elif period == 'a.m.':
            hour = hours
            return f"{hour}:{minutes}"
        
        # converts p.m. period to proper hour based on 24-Hours-Format
        if period == 'p.m.':
            if len(hours) < 2:
                hours = '0' + hours
                
            try:
                hour = P_M_CONVERTER[hours]
            except:
                raise ValueError("Invalid Timeinput.")
            
        # prepare a string with formatted values    
            time_24 = f"{hour}:{minutes}"
        
        # returns list with 24H Format 
            return time_24
    
    # checks if the time is given in 24 Hours Format
    elif len(time.split()) < 2:
        return time
    
    else:
        raise ValueError("Invalid Timeinput.")
        


def convert(time: str) -> float:
    """Converts time from a 24h formatted string to the corresponding number of hours as a float in decimal time format.

    Args:
        time (str): timestring in 24-hour format

    Returns:
        float: the corresponding number of hours as a float (time as hours in decimal format)
    """
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


if __name__ == '__main__':
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