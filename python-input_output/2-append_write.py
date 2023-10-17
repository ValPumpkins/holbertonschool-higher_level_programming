#!/usr/bin/python3
""" Function to append in file """


def append_write(filename="", text=""):
    """ Function to append in file """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
