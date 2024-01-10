#!/usr/bin/python3
"""Creating a class that raises an exception"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creating a derived class of BaseGeometry

    private instancess attributes:
    - width
    - height
    """
    def __init__(self, width, height):
        """initializing rectangle instnaces

        Args:
            width: width of the rectangle
            height: height of the Rectangle
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculating The area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Magic function that print the rectagle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


"""Creating another derived class"""


class Square(Rectangle):
    """Initialising the variable using the init function"""

    def __init__(self, size):
        """initialization method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
