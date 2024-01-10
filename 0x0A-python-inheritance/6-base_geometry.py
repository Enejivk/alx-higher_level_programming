#!/usr/bin/python3
"""Creating a class that raise exeption"""


class BaseGeometry:
    """This class contain a method that will be used in raising exeption"""
    def area(self):
        raise Exception("area() is not implemented")
