#!/usr/bin/python3
"""This class is going to return a matrix"""

        
class MyList(list):
    def print_sorted(self):
        new_list_ = self.copy()
        new_list_.sort()
        print(new_list_)