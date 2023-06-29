##### HOW TO TEST #####

"""Here’s how to test your code manually:

Run your program with python response.py.
Ensure your program prompts you for an email, 
then type malan@harvard.edu, followed by Enter. 
Your program should output Valid.

Run your program with python response.py. 
Type your own email, followed by Enter. 
Your program should output Valid.

Run your program with python response.py. 
Type malan@@@harvard.edu, followed by Enter.
Your program should output Invalid.

Run your program with python response.py. 
Mistype your own email, including an extra . before .com, for example. 
Press enter and your program should output Invalid.

You can execute the below to check your code using check50, 
a program that CS50 will use to test your code when you submit. 
But be sure to test it yourself as well!

check50 cs50/problems/2022/python/response"""
from response import validate_email


def test_validate_email_instructions_valid_mail():
    """Tests the testcases from the instructions, with valid email format inputs."""
    # test a valid and real email 
    assert validate_email("malan@harvard.edu") == "Valid."
    # test random email with proper format
    assert validate_email("test1234@gmail.com") == "Valid."
    
    
def test_validate_email_instructions_invalid_mail():
    """Tests the testcases from the instructions, with invalid email format inputs. """
    # test invalid email format from test instructions
    assert validate_email("malan@@@harvard.edu") == "Invalid."
    # test unusual punctuation in the email 
    assert validate_email("test1234@gmail..com") == "Invalid."
    

def test_validate_email_cornercases():
    """Tests cornercases with incorrect formatted input."""
    # try to input an url as email
    assert validate_email("www.google.com") == "Invalid."
    # email without containing any @ character
    assert validate_email("Aloha_World.com") == "Invalid."
    # test without a given domain in email
    assert validate_email("test123@xyz") == "Invalid."