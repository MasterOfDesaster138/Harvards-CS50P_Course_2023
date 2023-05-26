"""
    Title: Problemset_0 - Einstein

    Author: Emely Benke
    
    Created: 2023-05-26
    
    Version: 0.1
    
    Summary:
            Even if you haven’t studied physics (recently or ever!), you might have heard that E=mc², 
            wherein 'E' represents energy (measured in Joules), 
            'm' represents mass (measured in kilograms), and 
            'c' represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. 
            Essentially, the formula means that mass and energy are equivalent.

            In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
            and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""
SPEED_OF_LIGHT = 300000000 # meters per second

mass = int(input("What's the given mass in kilograms?: ")) # convert str to int for calculation 

energy = mass * SPEED_OF_LIGHT **2 # E = mc²

# output = f"Calculated energy measured in Joules is: {energy} for given mass."
print(energy)

