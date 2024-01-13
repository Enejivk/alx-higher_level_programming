#!/usr/bin/python3
"""
This function write to a file
return the numbers of character written
"""


def write_file(filename="", text=""):
    """write_file: the funtion write to a file

    Args:
        filename: This contain the name of file to be written.
        text: This contain all the text to be written to the file.

    Returns:
        It return the total character written
    """
    with open(filename, "w", encoding="utf8") as file:
        written = file.write(text)
        return written
