#!/usr/bin/python3

""" Class square that defines a square """


class Square:
    """ Class Square that defines a square w/ size """

    def __init__(self, size=0):
        """
        Initialize new square w/ optionnal size
        Args:
            size (int, optionnal): size of square. Default is 0
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to get the size attribute
        Return:
            size (int): square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the square size

        Args:
            Value (int): square size
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return area of square
        Return:
            int: square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square w/ the '#' char in stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
