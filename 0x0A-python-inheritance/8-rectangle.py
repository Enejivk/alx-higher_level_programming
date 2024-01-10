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


        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
