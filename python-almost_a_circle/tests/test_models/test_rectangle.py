#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest
import io
import sys


from tests.test_models.test_base import TestBase
from models.rectangle import Rectangle


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    # ATTRIBUTES
    def test_valid_attributes(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    """ Testing invalid attributes """

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle("hello", 20, 5, 5)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, None, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 5, 5)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, None, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "hello", 5)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, None)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "hello")

    # AREA
    def test_area(self):
        """ Testing area """
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.area(), 200)

    def test_area_large(self):
        """ Testing large area """
        rect = Rectangle(1000, 2000, 500, 500)
        self.assertEqual(rect.area(), 2000000)

    def test_area_zero(self):
        """ Testing zero area """
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0)

    # DISPLAY
    def test_display(self):
        """ Testing display """
        rect = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###"
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue().strip(), expected_output)

    def test_display_x_y(self):
        """ Testing display with x and y coordinates """
        rect = Rectangle(3, 2, 2, 1, 42)
        expected_output = '\n  ###\n  ###\n'
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_display_zero_x_y(self):
        """ Testing display with x and y coordinates """
        rect = Rectangle(3, 2, 0, 0, 99)
        expected_output = '###\n###\n'
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_display_large_x_y(self):
        """ Testing display with x and y coordinates """
        rect = Rectangle(2, 2, 5, 3, 10)
        expected_output = '\n\n\n     ##\n     ##\n'
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue(), expected_output)

    # STRING REP
    def test_str_representation(self):
        rect = Rectangle(5, 4, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 5/4"
        self.assertEqual(str(rect), expected_str)

    def test_str_representation_with_zero_coordinates(self):
        rect = Rectangle(3, 3, 0, 0, 99)
        expected_str = "[Rectangle] (99) 0/0 - 3/3"
        self.assertEqual(str(rect), expected_str)

    def test_str_representation_with_negative_id(self):
        rect = Rectangle(2, 2, 2, 2, -1)
        expected_str = "[Rectangle] (-1) 2/2 - 2/2"
        self.assertEqual(str(rect), expected_str)

if __name__ == '__main__':
    unittest.main()
