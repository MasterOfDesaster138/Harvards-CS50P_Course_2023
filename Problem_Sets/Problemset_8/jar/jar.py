"""
Title: Problemset_8 - Cookiejar

Author: Emely Benke

Created: 2023-07-07

Version: 0.1

Summary:
Suppose that you’d like to implement a cookie jar in which to store cookies.
In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity,
which represents the maximum number of cookies that can fit in the cookie jar.
If capacity is not a non-negative int, though,
__init__ should instead raise a ValueError.

__str__ should return a str with 🍪,
where is the number of cookies in the cookie jar.
For instance, if there are 3 cookies in the cookie jar,
then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar.
If adding that many would exceed the cookie jar’s capacity,
though, deposit should instead raise a ValueError.

withdraw should remove n cookies from the cookie jar.
Nom nom nom. If there aren’t that many cookies in the cookie jar,
though, withdraw should instead raise a ValueError.

capacity should return the cookie jar’s capacity.

size should return the number of cookies actually in the cookie jar.

Structure your class per the below.
You may not alter these methods’ parameters,
but you may add your own methods.

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

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

class Jar:
    """A class representing a cookie jar.

    Args:
        capacity (int, optional): The maximum capacity of the jar. Defaults to 12.
        size (int, optional): The current number of cookies in the jar. Defaults to 0.

    Attributes:
        capacity (int): The maximum capacity of the jar.
        size (int): The current number of cookies in the jar.

    Raises:
        ValueError: If the maximum capacity or size is set to an invalid value.

    """

    def __init__(self, capacity: int = 12, size: int = 0) -> None:
        self.capacity = capacity
        self.size = size

    def __str__(self):
        """Returns a string representation of the jar using cookie emojis."""
        return "🍪" * self.size

    def deposit(self, number: int) -> None:
        """Deposits cookies into the jar.

        Args:
            n (int): The number of cookies to deposit.

        Raises:
            ValueError: If the maximum capacity of the jar is exceeded.

        """
        if (self.size + number) > self.capacity:
            raise ValueError("Maximum capacity has been exceeded")
        else:
            self.size += number

    def withdraw(self, number: int) -> None:
        """Withdraws cookies from the jar.

        Args:
            n (int): The number of cookies to withdraw.

        Raises:
            ValueError: If the jar doesn't have enough cookies to withdraw.

        """
        if (self.size - number) < 0:
            raise ValueError("The cookie jar has been empty for a long time")
        else:
            self.size -= number

    @property
    def capacity(self) -> int:
        """The maximum capacity of the jar."""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        """Sets the maximum capacity of the jar.

        Args:
            capacity (int): The maximum capacity of the jar.

        Raises:
            ValueError: If the capacity is not a positive number.

        """
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Not a positive number")

    @property
    def size(self):
        """The current number of cookies in the jar."""
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        """Sets the current number of cookies in the jar.

        Args:
            size (int): The current number of cookies in the jar.

        Raises:
            ValueError: If the size is a negative number.

        """
        if size < 0:
            raise ValueError("Cookies are out")
        else:
            self._size = size
