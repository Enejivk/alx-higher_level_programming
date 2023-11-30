#!/usr/bin/python3
def islower(c):
    ascii_upper = ord(c)
    if ascii_upper <= 122 and ascii_upper >= 97:
        return True
    else:
        return False
