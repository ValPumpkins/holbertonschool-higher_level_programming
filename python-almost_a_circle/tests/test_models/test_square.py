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
        square = Square(5)
        self.assertTrue(isinstance(square, Rectangle),
                        "Square should inherit from Rectangle")

    # INIT
    def test_square_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

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

    # SIZE VALIDATION
    def test_size_getter(self):
        """ Testing size getter """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """ Testing size setter """
        square = Square(5, 2, 3, 1)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_size_setter_negative(self):
        """ Testing size setter with negative value """
        with self.assertRaises(ValueError):
            square = Square(5)
            square.size = -10

    def test_size_setter_zero(self):
        """ Testing size setter with zero value """
        with self.assertRaises(ValueError):
            square = Square(5, 2, 3, 1)
            square.size = 0

    def test_size_setter_float(self):
        """ Testing size setter with float value """
        with self.assertRaises(TypeError):
            square = Square(5, 2, 3, 1)
            square.size = 3.14

    def test_size_setter_string(self):
        """ Testing size setter with string value """
        with self.assertRaises(TypeError):
            square = Square(5, 2, 3, 1)
            square.size = "hello"

    # UPDATE
    def test_update_args(self):
        """ Testing square initialization with args """
        square = Square(3, 1, 2, 42)
        square.update(1, 4, 3, 0, 0)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 0)

    def test_update_kwargs_only(self):
        """ Testing square initialization with kwargs """
        square = Square(3, 1, 2, 42)
        square.update(size=4, x=3, y=0, id=1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 0)

    def test_update_kwargs_args1(self):
        """ Testing square initialization with kwargs """
        square = Square(3, 1, 2, 42)
        square.update(1, 4, size=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_args_kwargs2(self):
        square = Square(3, 1, 2, 42)
        square.update(1, size=4, x=0)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_unknown_attributes(self):
        """ Testing update with unknown attributes """
        square = Square(3, 2, 4, 5)
        square.update(1, size=4, x=0)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 4)


if __name__ == "__main__":
    unittest.main()
