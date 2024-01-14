#!/usr/bin/python3
"""This funtion return a dictionary of all the attribute"""


def class_to_json(obj):
    """ This function returns a dictionary representation of obj"""
    return vars(obj)
