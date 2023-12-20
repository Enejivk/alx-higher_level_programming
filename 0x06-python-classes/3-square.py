#!/usr/bin/python3
"""Creating a class"""


class Square:
    """Creating an attribute"""
    def __init__(self, size=0):

        """Validating the value"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """Initialising size"""
            self.__size = size

    def area(self):
        return self.__size**2
