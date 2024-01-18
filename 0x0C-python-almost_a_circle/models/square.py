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
        self.size = size

    def __str__(self):
        """Return string rep. of attribute
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
