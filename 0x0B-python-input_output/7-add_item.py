#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Importing the module the module need"""


mylist = []
for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
mylist.extend(my_list)
save_to_json_file(mylist, "add_item.json")
