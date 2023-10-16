#!/usr/bin/python3
""" Check if object is an instance of a class that inherited from a_class """


def inherits_from(obj, a_class):
    """ Check if object is an instance of a class that inherited from a_class
    Args:
        obj: object to check
        a_class: class to compare with
    Returns:
        True : obj is instance of a_class or class that inherited from a_class
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
