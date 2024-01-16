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
