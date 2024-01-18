#!/usr/bin/python3
"""module that inherite from a rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Return string rep. of attribute
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:

            raise ValueError("width must be > 0")
        else:
            self.__size = value

    def update(self, *args, **kwargs):
        """printing the value of attribute
        """

        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "y":
                    self.y = kwargs["y"]
                if key == "x":
                    self.x = kwargs["x"]
