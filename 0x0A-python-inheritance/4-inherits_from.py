#!/usr/bin/python3
"""
Checking if it belongs to a class or subclass directly or indirectly

Args:
- obj: The objecct to check
- a_class: The class to check against.

return:
-Ture if the object is an instance of a class that inherited from a
a class or false otherwise.
"""


def inherits_from(obj, a_class):
    """Checking if it belons to the same class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
