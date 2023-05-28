"""
   Title: Problemset_2 - Coke Machine

    Author: Emely Benke
    
    Created: 2023-05-27
    
    Version: 0.1
    
    Summary: 
            The U.S. Food & Drug Adminstration (FDA) offers 
            downloadable/printable posters that “show nutrition information 
            for the 20 most frequently consumed raw fruits … in the United States. 
            Retail stores are welcome to download the posters, 
            print, display and/or distribute them to consumers 
            in close proximity to the relevant foods in the stores.”

            In a file called nutrition.py, implement a program 
            that prompts consumers users to 
            input a fruit (case-insensitively) 
            and then outputs the number of calories 
            in one portion of that fruit,
            per the FDA’s poster for fruits, 
            which is also available as text. 
            Capitalization aside, assume that users will 
            input fruits exactly as written in the poster 
            (e.g., strawberries, not strawberry). 
            Ignore any input that isn’t a fruit.
"""

fruit_dataset = { # ['fruit_name': list with fruitdata ]
    'columns':          ('Calories','Calories from Fat','Sugars','Protein','Vitamin A', 'Vitamin C', 'Calcium', 'Iron'),
    'units':            ('cal', 'cal', 'g', 'mg', 'mg', 'g', 'g', 'g', '%DV', '%DV', '%DV', '%DV'),             
    'apple':            [130, 0, 0, 0, 260, 34, 5, 25, 1, 2, 8, 2, 2],
    'avocado':          [50, 35, 4.5, 0, 140, 3, 1, 0, 1, 0, 4, 0, 2],
    'banana':           [110, 0, 0, 0, 450, 30, 3, 19, 1, 2, 15, 0, 2],
    'cantaloupe':       [50, 0, 0, 20, 240, 12, 1, 11, 1, 120, 80, 2, 2],
    'grapefruit':       [60, 0, 0, 0, 160, 15, 2, 11, 1, 35, 100, 4, 0],
    'grapes':           [90, 0, 0, 15, 240, 23, 1, 20, 0 , 0, 2, 2, 0],
    'honeydew melon':   [50, 0, 0, 30, 210, 12, 1, 11, 1, 2, 45, 2, 2],
    'kiwifruit':        [90, 10, 1, 0, 450, 20, 4, 13, 1, 2, 240, 4, 2],
    'lemon':            [15, 0, 0, 0, 75, 5, 2, 2, 0, 0, 40, 2, 0],
    'lime':             [20, 0, 0, 0, 75, 7, 2, 0, 0, 0, 35, 0, 0],
    'nectarine':        [60, 5, 0.5, 0, 250, 15, 2, 11, 1, 8, 15, 0, 2],
    'orange':           [80, 0, 0, 0, 250, 19, 3, 14, 1, 2, 130, 6, 0],
    'peach':            [60, 5, 0.5, 0, 230, 15, 2, 13, 1, 6, 15, 0, 2],
    'pear':             [100, 0, 0, 0, 190, 26, 6, 16, 1, 0, 10, 2, 0],
    'pineapple':        [50, 0 , 0, 10, 120, 13, 1, 10, 1, 2, 50, 2, 2],
    'plums':            [70, 0, 0, 0, 230, 19, 2, 16, 1, 8 , 10, 0, 2],
    'strawberries':     [50, 0, 0, 0, 170, 11, 2, 8, 1, 0, 160, 2, 2],
    'sweet cherries':   [100, 0, 0, 0, 350, 26, 1, 16, 1, 2, 15, 2, 2],
    'tangerine':        [50, 0, 0, 0, 160, 13, 2, 9, 1, 6, 45, 4, 0],
    'watermelon':       [80, 0, 0, 0, 270, 21, 1, 20, 1, 30, 25, 2, 4],
}

def main():
    # prompt a fruit from user
    fruit_input = user_input_handling()
    
    # search inputted fruit in FDA-Dataset + Output Data
    fruit_info = match_fruit(fruit_input)
    

def user_input_handling() -> str:
    while True:
        prompt = input("Type a Fruit: ").strip()
        if prompt.lower() in fruit_dataset.keys():
            return prompt.lower()
        else:
            print('Inputted Fruit not found in FDA-Dataset. \n', 'Try another!')

def match_fruit(fruit:str) -> str:
    # fetch list with values from dataset 
    fruit_data = fruit_dataset[fruit]
    
    # output fruit name and calories 
    print(f"Calories: {fruit_data[0]}")


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