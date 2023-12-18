#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide = a/b
        return divide
    except ZeroDivisionError:
        divide = None
        return divide
    finally:
        print("Inside result: {}".format(divide))
