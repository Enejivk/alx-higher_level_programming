#!/usr/bin/python3
"""Creating a Rectangle class"""


class Rectangle:
    """Creating a class attribute"""
    number_of_instances = 0
    """Creating a private instance of width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """Increasing the class attribute"""
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        rectanglePattern = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectanglePattern += "#"
            rectanglePattern += "\n"
        return rectanglePattern[:-1]

    def __repr__(self):
        """It return the string representation that can be passed to oval()"""
        return "Rectangle({}, {})" .format(self.__width, self.__height)

    def __del__(self):
        """checking if instance rectangle was deleted"""
        print("Bye rectangle...")
        """Decreasing the class attribute"""
        Rectangle.number_of_instances -= 1
