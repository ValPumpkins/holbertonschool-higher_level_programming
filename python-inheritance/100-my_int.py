#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """ invert True & False
    Args:
        int (int): mother class
    """
    def __eq__(self, number):
        return super().__ne__(number)

    def __ne__(self, number):
        return super().__eq__(number)
