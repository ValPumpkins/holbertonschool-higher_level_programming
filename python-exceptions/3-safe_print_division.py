#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divisionResult = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        divisionResult = None
    finally:
        print("Inside result: {}".format(divisionResult))

    return divisionResult
