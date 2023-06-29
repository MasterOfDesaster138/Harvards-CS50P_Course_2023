""" 
    Title: Problemset_7 - Working 9 to 5

    Author: Emely Benke
    
    Created: 2023-06-28
    
    Version: 0.1
    
    Summary:
            Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, 
            instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), 
            wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, 
            wherein “meridiem” means midday (i.e., noon).

            Conversion Table:
            12-Hour    24-Hour
            -----------------
            12:00 AM	00:00
            1:00 AM	    01:00
            2:00 AM	    02:00
            3:00 AM	    03:00
            4:00 AM	    04:00
            5:00 AM	    05:00
            6:00 AM	    06:00
            7:00 AM	    07:00
            8:00 AM	    08:00
            9:00 AM	    09:00
            10:00 AM	10:00
            11:00 AM	11:00
            12:00 PM	12:00
            1:00 PM	    13:00
            2:00 PM	    14:00
            3:00 PM	    15:00
            4:00 PM	    16:00
            5:00 PM	    17:00
            6:00 PM	    18:00
            7:00 PM	    19:00
            8:00 PM	    20:00
            9:00 PM	    21:00
            10:00 PM	22:00
            11:00 PM	23:00
            12:00 AM	00:00
            
            In a file called working.py, implement a function called convert that expects a str 
            in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
            Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. 
            Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

            9:00 AM to 5:00 PM
            9 AM to 5 PM
            Raise a ValueError instead if the input to convert is not in either of those formats 
            or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
            But do not assume that someone’s hours will start ante meridiem and end post meridiem; 
            someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

            Structure working.py as follows, wherein you’re welcome to modify main and/or 
            implement other functions as you see fit, but you may not import any other libraries. 
            You’re welcome, but not required, to use re and/or sys.
            
            Either before or after you implement convert in working.py, additionally implement, 
            in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, 
            each of whose names should begin with test_ so that you can execute your tests with:
            --> pytest test_working.py
"""
"""Hints:
Recall that the re module comes with quite a few functions, 
per docs.python.org/3/library/re.html, including search.

Recall that regular expressions support quite a few special characters, 
per docs.python.org/3/library/re.html#regular-expression-syntax.

Because backslashes in regular expressions could be mistaken for escape sequences (like \n), 
best to use Python’s raw string notation for regular expression patterns, 
else pytest will warn with DeprecationWarning: invalid escape sequence. 
Just as format strings are prefixed with f, so are raw strings prefixed with r. 
For instance, instead of "harvard\.edu", use r"harvard\.edu".

Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” 
per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, 
which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, 
or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.

Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax. 
"""
# IMPORTS: 
import re


def main():
    print(convert(input("Hours: ")))


def convert(time_str: str) -> str:
    """
    Convert a time string from 12-hour format to 24-hour format.

    Args:
        time_str (str): A string representing the time in one of the following formats:
                        - "9 AM to 5 PM"
                        - "9:00 AM to 5:00 PM"

    Returns:
        str: The corresponding time string in 24-hour format.

    Raises:
        ValueError: If the input time string is not in the expected formats or if the time values are invalid.
    """
    # Check if the input matches one of the expected formats
    pattern1 = r"(\d+)(:\d+)?\s+([AP]M)"
    pattern2 = r"Type\s+(\d+)(:\d+)?\s+([AP]M)"
    
    if not re.match(pattern1, time_str) and not re.match(pattern2, time_str):
        raise ValueError("Invalid input format")

    # catch incorrect separator of the 2 given times
    if 'to' not in time_str:
        raise ValueError("Invalid data separator")
    # Split the start and end times
    start_time, end_time = time_str.split(" to ")

    # Check and convert the start time
    match = re.search(r"\d+", start_time)
    start_hour = int(match.group())
    # check if the given input is in the valid range
    if start_hour < 0 or start_hour > 12:
        raise ValueError("Incorrect input")
         
    # collect minutes if provided 
    if re.search(r"\d+:\d+", start_time):
        start_minutes = int(start_time.split(":")[1].split()[0])
    else: # otherwise set the default value to 0 minutes
        start_minutes = 0
    # determine the given abbreviation 
    if "AM" in start_time:
        time_format = "AM"
    elif "PM" in start_time:
        time_format = "PM"
    # transform hours from 12H to 24H format
    if time_format == "PM" and start_hour != 12:
        start_hour += 12
    elif time_format == "AM" and start_hour == 12:
        start_hour = 0

    # Check and convert the end time
    match = re.search(r"\d+", end_time)
    end_hour = int(match.group())
    
    # check if the given input is in the valid range
    if 0 > end_hour > 12:
        raise ValueError("Incorrect input")
    
    # collect minutes if provided 
    if re.search(r"\d+:\d+", end_time):
        end_minutes = int(end_time.split(":")[1].split()[0])
    else: # otherwise set the default value to 0 minutes
        end_minutes = 0
    # determine the given abbreviation 
    if "AM" in end_time:
        time_format = "AM"
    elif "PM" in end_time:
        time_format = "PM"
    # transform hours from 12H to 24H format
    if time_format == "PM" and end_hour != 12:
        end_hour += 12
    elif time_format == "AM" and end_hour == 12:
        end_hour = 0
    
    # Check if the time values are valid
    if not (0 <= start_hour <= 23 and 0 <= start_minutes <= 59):
        raise ValueError("Invalid start time")
    if not (0 <= end_hour <= 23 and 0 <= end_minutes <= 59):
        raise ValueError("Invalid end time")
    # Format and return the result
    return f"{start_hour:02d}:{start_minutes:02d} to {end_hour:02d}:{end_minutes:02d}"



if __name__ == "__main__":
    main()
    
    
    
"""How to Test working.py
Here’s how to test working.py manually:

Run your program with python working.py. Ensure your program prompts you for a time. 
Type 9 AM to 5 PM, followed by Enter. Your program should output 09:00 to 17:00.

Run your program with python working.py. 
Type 9:00 AM to 5:00 PM, followed by Enter. Your program should again output 09:00 to 17:00.

Run your program with python working.py. Ensure your program prompts you for a time. 
Type 10 PM to 8 AM, followed by Enter. Your program should output 22:00 to 08:00.

Run your program with python working.py. Ensure your program prompts you for a time. 
Type 10:30 PM to 8:50 AM, followed by Enter. Your program should again output 22:30 to 08:50.

Run your program with python working.py. Ensure your program prompts you for a time. 
Try intentionally inducing a ValueError by typing 9:60 AM to 5:60 PM, followed by Enter. 
Your program should indeed raise a ValueError.

Run your program with python working.py. Ensure your program prompts you for a time. 
Try intentionally inducing a ValueError by typing 9 AM - 5 PM, followed by Enter. 
Your program should indeed raise a ValueError.

Run your program with python working.py. Ensure your program prompts you for a time. 
Try intentionally inducing a ValueError by typing 09:00 AM - 17:00 PM, followed by Enter. 
Your program should indeed raise a ValueError."""