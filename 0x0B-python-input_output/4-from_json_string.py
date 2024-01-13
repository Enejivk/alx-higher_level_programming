#!/usr/bin/python3
"""jason reprsentation of a dictionary"""
import json


def from_json_string(my_str):
    """This funtion return a dictionary"""
    return json.loads(my_str)
