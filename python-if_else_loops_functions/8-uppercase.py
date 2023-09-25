#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercaseChar = chr(ord(char) - 32)
            print("{}".format(uppercaseChar), end="")
        else:
            print("{}".format(char), end="")
    print()
