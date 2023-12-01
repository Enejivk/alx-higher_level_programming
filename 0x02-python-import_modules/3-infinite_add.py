#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    sum_all = 0
    for i in range(1, n):
        num = int(sys.argv[i])
        sum_all = sum_all + num
    print("{}".format(sum_all))
