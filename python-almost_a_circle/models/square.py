#!/usr/bin/python3
""" Defines a square class """

from models.rectangle import Rectangle


class Square (Rectangle):
    """ Represent a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a square
        Args:
            size (int): size of new square
            x (int): x-coordinate of new square
            y (int): y-coordinate of new square
            id (int): id of new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set size of square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return string representation of a square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
