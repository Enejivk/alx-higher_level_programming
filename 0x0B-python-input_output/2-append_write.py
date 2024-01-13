#!/usr/bin/python3
"""
This funtion append to a file and return the total numbers of character append
"""


def append_write(filename="", text=""):
    """This append content to a file"""
    with open(filename, "a", encoding="utf8") as file:
        return file.write(text)
