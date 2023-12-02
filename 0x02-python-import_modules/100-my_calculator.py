#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    lent = len(argv)
    if lent < 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    operator = argv[2]
    n2 = int(argv[3])
    match operator:
        case "+":
            print("{} + {} = {}".format(n1, n2, add(n1, n2)))
        case "-":
            print("{} - {} = {}".format(n1, n2, sub(n1, n2)))
        case "/":
            print("{} / {} = {}".format(n1, n2, div(n1, n2)))
        case "*":
            print("{} * {} = {}".format(n1, n2, mul(n1, n2)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
