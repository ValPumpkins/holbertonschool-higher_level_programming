#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keytoDelete = []

    for key, val in a_dictionary.items():
        if val == value:
            keytoDelete.append(key)

    for key in keytoDelete:
        del a_dictionary[key]

    return a_dictionary
