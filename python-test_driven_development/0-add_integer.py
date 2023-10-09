#!/usr/bin/python3

""" Func thats add 2 integers """


def add_integer(a, b=98):
    """
    Args:
        a (int or float): first integer
        b (int or float): second integer
    Returns:
        int: sum of a and b
    Raises:
        TypeError: if a or b is not an integer or float
    """
    
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
