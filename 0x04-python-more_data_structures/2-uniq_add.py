#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = []
    result = 0
    for num in my_list:
        if num not in unique_num:
            unique_num.append(num)
            result = result + num
    return result 