#!/usr/bin/python
import json
"""save save string to json file"""


def save_to_json_file(my_obj, filename):
    """convert a string to json representation and save"""
    with open(filename, "w", encoding="utf8") as file:
        file.write(json.dumps(my_obj))
