#!/usr/bin/python3
"""Creating a class"""


class Square:
    def __init__(self, size=0):

        """Condition for initialization"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute the area of the square"""
        return self.__size * self.__size
