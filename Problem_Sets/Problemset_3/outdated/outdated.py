"""
   Title: Problemset_3 - Outdated

    Author: Emely Benke
    
    Created: 2023-05-28
    
    Version: 0.1
    
    Summary: 
            In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), 
            otherwise known as middle-endian order, which is arguably bad design. 
            Dates in that format can’t be easily sorted because the date’s year comes last instead of first. 
            Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). 
            Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, 
            but 9/8/1636 could also be interpreted as August 9, 1636!

            Fortunately, computers tend to use ISO 8601, an international standard that prescribes 
            that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, 
            formatting years with four digits, months with two digits, 
            and days with two digits, “padding” each with leading zeroes as needed.

            In a file called outdated.py, implement a program that prompts the user for a date, 
            anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
            wherein the month in the latter might be any of the values in the list below:
            
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]

            Then output that same date in YYYY-MM-DD format. 
            If the user’s input is not a valid date in either format, prompt the user again. 
            Assume that every month has no more than 31 days; 
            no need to validate whether a month has 28, 29, 30, or 31 days.
"""

def main():
    # prompting a date input
    date_list = get_input() # [month, day, year]
    # transform given date to proper format
    date_str = format_date(date_list)
    # output the formatted date string
    print(date_str)
    

def get_input() -> str:
    """Prompt and validate a date in month-day-year order.
        Accepts follwing Formats:
            -> 9/8/1636
            -> September 8, 1636"""
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    while True:
        user_input = input("Date: ").strip()
        
        try:
            # check for dateformat like [9/8/1636]
            if '/' in user_input:
                # separate the values in a list
                date_list = user_input.split('/')
                # convert date values to int for comparsion operations
                month, day, year = int(date_list[0]), int(date_list[1]), int(date_list[2])
                # validate if day + month + year are in proper range
                date_valid = validate_date_range(month, day, year)
                if date_valid:
                    return date_list
                else:
                    raise ValueError("Given Date not in proper Range. Try Again!")
              
            # handle dateformat like [September 8, 1636]
            else:
                # transform the input to a list of values
                date_list = user_input.split()
                # remove a comma after day
                date_list[1] = date_list[1].removesuffix(',')
                # validate the inputted values 
                if date_list[0] in months:                                   # -> check if full month name matches a month in list 
                    month = months.index(date_list[0]) + 1                   # transform month name to a number
                    date_list[0] = str(month)                                # update the date_list
                    day, year = int(date_list[1]), int(date_list[2])         # convert strings to integers
                    date_valid = validate_date_range(month, day, year)       # check if given day + month + year are in proper range
                    if date_valid:
                        return date_list
            
        except:
            pass                                                           
                        

def validate_date_range(month: int, day: int, year: int) -> bool:
    # check for proper range
    if 0 < month < 13 and 0 < day < 32 and 0 < year: # no max for year
        # check length of each values
        if len(str(day)) > 0 and len(str(month)) > 0 and len(str(year)) == 4:
            return True
    else:
        return False


def format_date(date_list: list) -> str:
    """Tranform date format to YYYY-MM-DD."""
    # unpack date_list
    month, day, year = date_list
    
    # fill up day and month with leading 0 if needed
    if len(month) < 2:
        month = '0' + month
    if len(day) < 2:
        day = '0' + day
    
    return f"{year}-{month}-{day}"


if __name__ == '__main__':
    main()
    
    
    
"""Here’s how to test your code manually:

Run your program with python outdated.py. Type 9/8/1636 and press Enter. 
Your program should output:
    1636-09-08

Run your program with python outdated.py. Type September 8, 1636 and press Enter. 
Your program should output:
    1636-09-08

Run your program with python outdated.py. Type 23/6/1912 and press Enter. 
Your program should reprompt the user.

Run your program with python outdated.py. Type December 80, 1980 and press Enter. 
Your program should reprompt the user."""



"""check50 cs50/problems/2022/python/outdated"""