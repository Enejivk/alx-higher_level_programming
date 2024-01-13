#!/usr/bin/python3
"""save save string to json file"""
import json


def save_to_json_file(my_obj, filename):
    """convert a string to json representation and save"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
