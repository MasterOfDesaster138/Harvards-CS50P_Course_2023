"""This is a Python file created for testing purposes of lines.py -> SLOC == 14, LOC == 22"""

# a random comment
def hello(name: str = "World") -> str:
    """Creates a greeting for the given name.

    Args:
        name (str, optional): name of a person or object. Defaults to "World".

    Returns:
        str: individual greeting message
    """
    return f"Hello, {name}!"


def main():
    output = hello()
    print(output)
    
    
if __name__ == '__main__':
    main()