#!/usr/bin/python3
""" Writes a string to a txt file and returns nb of char written """


def write_file(filename="", text=""):
    """ Writes a string to a txt file and returns nb of char written """

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
