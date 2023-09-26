#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    nbArguments = len(arguments)

    if nbArguments == 0:
        print("0 arguments.")
    elif nbArguments == 1:
        print("1 argument: ")
        print("1: {}".format(arguments[0]))
    else:
        print("{} arguments:".format(nbArguments))

        for i, argument in enumerate(arguments, 1):
            print("{}: {}".format(i, argument))
