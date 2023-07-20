""" 
Either before or after you implement jar.py, 
additionally implement, in a file called test_jar.py, 
four or more functions that collectively test 
your implementation of Jar thoroughly, 
each of whose names should begin with test_ 
so that you can execute your tests with:

pytest test_jar.py
Note that it’s not as easy to test 
instance methods as it is to test functions alone, 
since instance methods sometimes manipulate the same “state” (i.e., instance variables). 
To test one method (e.g., withdraw), then, 
you might need to call another method first (e.g., deposit). 
But the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing methods, 
as with Python’s own mock object library, 
so that you can call just the one method but modify the underlying state first, 
without calling the other method to do so.

For simplicity, though, no need to mock any state. 
Implement your tests as you normally would!
"""

""" 
Here’s how to test your code manually:

Open your test_jar.py file and import your Jar class with from jar import Jar. 
Create a function called test_init, wherein you create a new instance of Jar with jar = Jar(). 
assert that this jar has the capacity it should, then run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_str. 
In test_str, create a new instance of your Jar class and deposit a few cookies. 
assert that str(jar) prints out as many cookies as have been deposited, 
then run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_deposit. 
In test_deposit, create a new instance of your Jar class and deposit a few cookies. 
assert that the jar’s size attribute is as large as the number of cookies that have been deposited. 
Also assert that, if you deposit more than the jar’s capacity, deposit should raise a ValueError.
Run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_withdraw. 
In test_withdraw, create a new instance of your Jar class and first deposit a few cookies. 
assert that withdrawing from the jar leaves the appropriate number of cookies in the jar’s size attribute. 
Also assert that, if you withdraw more than the jar’s size, withdraw should raise a ValueError. 
Run your tests with pytest test_jar.py.
"""
import pytest
from jar import Jar   # type: ignore


def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    

def test_init_optional_param():
    jar = Jar(capacity=20)
    assert jar.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar._size == 5
    with pytest.raises(ValueError) as exceinfo:
        jar.deposit(8)
    


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    
    jar.withdraw(2) 
    assert jar._size == 3
    
    with pytest.raises(ValueError) as exceinfo:
        jar.withdraw(9)