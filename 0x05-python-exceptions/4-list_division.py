#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            divid = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            divid = 0
            print("division by 0")
        except TypeError:
            divid = 0
            print("wrong type")
        except IndexError:
            divid = 0
            print("out of range")
        finally:
            new_list.append(divid)
    return new_list
