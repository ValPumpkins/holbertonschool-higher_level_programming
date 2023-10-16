#!/usr/bin/python3
""" Check if object is instance of a class """


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance of a class
    Args:
        obj: object
        a_class: class
    Return:
        True if object is instance of a class, False otherwise
    """
    return isinstance(obj, a_class)
