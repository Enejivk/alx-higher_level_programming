#!/usr/bin/python3
"""
This function opens a file
Read the content of the file
print the content of the file
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        readfile = file.read().strip()
        print(readfile)
