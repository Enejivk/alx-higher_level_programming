#!/usr/bin/python3
"""jason reprsentation of a dictionary"""
import json


def to_json_string(my_obj):
    """This funtion return a dictionary"""
    return json.dumps(my_obj, sort_keys="true")
