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
        """Reload_from_json: It takes an attribute of self
        and convert it to the respective value stored in json.
        Arg
        self: This contain all the attribute of the object
        json: This is contain the value to be replace with the value in 
        self.
        """
        self.age = json['age']
        self.first_name = json['first_name']
        self.last_name = json['last_name']