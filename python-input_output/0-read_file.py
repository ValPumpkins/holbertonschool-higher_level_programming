#!/usr/bin/python3
""" Reads txt files """


def read_file(filename=""):
    """ Reading file function """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
