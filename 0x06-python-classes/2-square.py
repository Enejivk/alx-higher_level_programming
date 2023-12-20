#!/usr/bin/python3
"""Creating a class"""


class Square:
    """Initialsing a class"""
    def __init__(self, size=0):
        """Validating and hadling error"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """Initialising my attribute"""
            self.__size = size
