#!/usr/bin/python3
""" MyInt class """

class MyInt(int):
    """ invert True & False
    Args:
        number (int): integer
    """
    def __eq__(self, number):
        return super().__ne__(number)

    def __ne__(self, number):
        return super().__eq__(number)
