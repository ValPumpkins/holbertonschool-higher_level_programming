#!/usr/bin/python3
""" Defines an inherited list class MyList """


class MyList (list):
    """ Implements sorted printing for the built-in list class """
    def print_sorted(self):
        """ Prints a list in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)
