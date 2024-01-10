#!/usr/bin/python3
"""Creatin a class my"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print list
        """
        print(sorted(self))
