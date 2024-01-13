#!/usr/bin/python3
"""Code that load content from a jsons file"""
import json


def load_from_json_file(filename):
    """Print the content of jason file"""
    with open(filename, "r", encoding="utf8") as file:
        fileread = file.read()
        return json.loads(fileread)
