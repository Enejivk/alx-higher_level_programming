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
        if attrs is None:
            return attribute_dict

        newattribute_dict = {}
        for key in attrs:
            if key in attribute_dict:
                newattribute_dict[key] = attribute_dict[key]
        return newattribute_dict

    def reload_from_json(self, json):
        """Reload_from_json: It takes an attribute of self"""
        for key in json:
            self.__dict__[key] = json[key]
