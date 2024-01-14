#!/usr/bin/python3
"""Add all the command line argurment to a list"""
import sys

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


mylist = []
for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
    """Extending the contennt of the initial list"""
my_list.extend(mylist)
save_to_json_file(my_list, "add_item.json")
