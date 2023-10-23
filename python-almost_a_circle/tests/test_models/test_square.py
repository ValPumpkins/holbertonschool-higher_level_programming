#!/usr/bin/python3
""" Unittest for Square class """

import unittest

from tests.test_models.test_rectangle import TestRectangle
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(TestRectangle):
    """ Testing Square Class """

    # INHERITANCE
    def test_square_inherits_from_rectangle(self):
        """ Testing inheritance """
        self.assertTrue(issubclass(Square, Rectangle),
                        "Square should inherit from Rectangle")

    # INIT
    def test_square(self):
        """ Testing square initialization """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    # STR REP
    def test_square_str_representation(self):
        """ Testing square string representation """
        square = Square(3, 1, 2, 42)
        self.assertEqual(str(square), "[Square] (42) 1/2 - 3")


if __name__ == "__main__":
    unittest.main()
