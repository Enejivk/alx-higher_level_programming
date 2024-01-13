#!/usr/bin/python3
"""
This function opens a file
Read the content of the file
print the content of the file
"""


def read_file(filename=""):
    """opening a file"""
    with open(filename, "r", encoding="utf-8") as file:
        readfile = file.read()
        print(readfile, end="")
