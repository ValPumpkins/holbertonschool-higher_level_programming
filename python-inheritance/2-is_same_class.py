#!/usr/bin/python3
""" Function that returns is instance if part of the class"""


def is_same_class(obj, a_class):
    """ Function that returns is instance if part of the class
    Args:
        obj: object
        a_class: class type
    Returns:
        True: if object is instance of a_class
        False: if not
     """
    return type(obj) is a_class
