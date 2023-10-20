#!/usr/bin/python3
""" Function to add attribute if possible """


def add_attribute(object, attribute_name, attribut_value):
    """ Add attribute if possible
    Args:
        object: object
        attribute_name: attribute name
        attribut_value: attribute value
    Raises:
        TypeError: when can't add a new attribute
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute_name, attribut_value)
