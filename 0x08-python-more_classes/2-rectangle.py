#!/usr/bin/python3
"""Creating a Rectangle class"""


class Rectangle:
    """Creating a private instance of width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that calculate parameter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        add_para = self.__height + self.__width
        return 2 * add_para
