#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as n
    a = 10
    b = 5
    print("{} + {} = {}" .format(a, b, n.add(a, b)))
    print("{} - {} = {}" .format(a, b, n.sub(a, b)))
    print("{} * {} = {}" .format(a, b, n.mul(a, b)))
    print("{} / {} = {}" .format(a, b, n.div(a, b)))
