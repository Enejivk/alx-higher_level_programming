#!/usr/bin/python3
"""Class"""


class Square:
    """
    Attribute
    """
    def __init__(self, size=0):
        """
        Initializing square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
