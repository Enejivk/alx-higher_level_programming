#!/usr/bin/python3
"""
Student class module
"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the conten of student module"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ It This funtion returns dictionary of all the attribute """
        attribute_dict = vars(self)
        if type(attrs) is list:

            for attr in attrs:
                if type(attr) is not str:
                    return attribute_dict

            new_attribute_dict = {}
            for key in attrs:
                if key in attribute_dict:
                    new_attribute_dict[key] = attribute_dict[key]
            return new_attribute_dict

        return attribute_dict
