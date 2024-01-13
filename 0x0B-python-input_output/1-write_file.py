#!/usr/bin/python3
"""
This function write to a file
return the numbers of character written
"""


def write_file(filename="", text=""):
    """write_file: the funtion write to a file"""
    with open(filename, "w", encoding="utf8") as file:
        return file.write(text)
