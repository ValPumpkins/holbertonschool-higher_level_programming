#!/usr/bin/python3
""" Class Square that inherits from class Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from class Rectangle """

    def __init__(self, size):
        """ Init a square
        Args:
            size (int): side size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns square area
        Returns:
            int: square area
        """
        return self.__size ** 2

    def __str__(self):
        """ Returns string representation of square """
        return "[Square] {}/{}".format(self.__size, self.__size)
