#!/usr/bin/python3
"""calculating rectagle module"""


from models.base import Base


class Rectangle(Base):
    """Rectagle class inherite from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """It initialize all the value
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:

            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:

            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:

            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:

            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calcuting the area of a rectagle"""
        return self.height * self.width

    def display(self):
        """Printing rectagle in form a # """
        for i in range(self.height):
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Print string represention of this object"""
        s = '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)
        return s

    def display(self):
        """printing a rectangle using #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """printing a list of value passed by command line argument"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "width":
                    self.width = kwargs["width"]
                if key == "height":
                    self.height = kwargs["height"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]
