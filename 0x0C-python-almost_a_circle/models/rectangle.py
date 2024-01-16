#!/usr/bin/python3
"""Creating a Base class
"""


class Base:
    """__nb_objects:
    Creating class attribute that keep tracks of the
    the numbers of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This function initialise value of id
        it checks if id is None if true it returns the number
        of object instead

        Args:
            id: holds the value of id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """Rectagle class inherite from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """It initialize all the value found in rectangle
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
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
