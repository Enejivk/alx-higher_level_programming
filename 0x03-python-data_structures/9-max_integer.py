#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    larget_number = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > larget_number:
            larget_number = my_list[i]
    return larget_number
