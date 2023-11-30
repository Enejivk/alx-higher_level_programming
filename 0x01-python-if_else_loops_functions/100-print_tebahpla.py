#!/usr/bin/python3
i = 90
while i > 64:
    j = i + 32
    print("{}{}".format(chr(i),chr(j)), end="")
    i=i-1