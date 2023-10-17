#!/usr/bin/python3
""" Class Rectangle that inherits from class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a rectangle"""

    def __init__(self, width, height):
        """ Initializes a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
