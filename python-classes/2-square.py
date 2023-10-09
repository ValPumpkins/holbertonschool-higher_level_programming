#!/usr/bin/python3

"""Classe square that defines a square """


class Square:
    """ Class Square that defines a square w/ size """

    def __init__(self, size=0):
        """
        Initialize new square w/ optionnal size

        Args:
            size (int, optionnal): size of square. Default is 0
        Raise:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
