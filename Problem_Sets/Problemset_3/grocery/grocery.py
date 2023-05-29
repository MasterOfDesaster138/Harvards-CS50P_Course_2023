"""
   Title: Problemset_3 - Grocery List

    Author: Emely Benke
    
    Created: 2023-05-29
    
    Version: 0.1
    
    Summary: 
            Suppose that you’re in the habit of making a list of items you need from the grocery store.

            In a file called grocery.py, implement a program that prompts the user for items, one per line, 
            until the user inputs control-d (which is a common way of ending one’s input to a program). 
            Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
            prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
            Treat the user’s input case-insensitively.
"""
def main():
    grocery_list = get_input()
    print_list(grocery_list)
    

def get_input() -> list:
    grocery_list = []
    while True:
        try: 
            # get user's input case-insensitively
            grocery_input = input().strip()
            # store every item in a list in uppercase
            grocery_list.append(grocery_input.upper())
        except KeyboardInterrupt:
            return grocery_list
            
        
def print_list(grocery_list: list):
    """Outputs the user’s grocery list in all uppercase, sorted alphabetically by item, 
    prefixing each line with the number of times the user inputted that item."""
    # create a set of grocery_list for removing all duplicates
    distinct_items = set(grocery_list)
    # sort distinct items alphabetically 
    item_list = sorted(list(distinct_items))
    
    # go through each item and prepare a string for output
    for item in item_list:
        # count the amount in grocery_list
        amount = grocery_list.count(item)
        print(f"{amount} {item}")


if __name__ == '__main__':
    main()
    

""""Here’s how to test your code manually:

Run your program with python grocery.py. Type mango and press Enter, then type strawberry and press Enter, followed by control-d. 
Your program should output:
1 MANGO
1 STRAWBERRY

Run your program with python grocery.py. Type milk and press Enter, then type milk again and press Enter, followed by control-d. 
Your program should output:
2 MILK

Run your program with python grocery.py. Type tortilla and press Enter, then type sweet potato and press Enter, followed by control-d. 
Your program should output:
1 SWEET POTATO
1 TORTILLA
"""

"""check50 cs50/problems/2022/python/grocery"""
