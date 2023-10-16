#!/usr/bin/python3
""" Defines class BaseGeometry """


class BaseGeometry:
    """ Represent class BaseGeometry """

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate a parameter as an int
        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an int
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
