#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    addition = 0

    for numbers in arguments:
        addition += int(numbers)
    print(addition)
