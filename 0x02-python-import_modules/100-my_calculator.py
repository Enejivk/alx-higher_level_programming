#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    lent = len(sys.argv)
    if lent < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    n1 = int(sys.argv[1])
    operator = sys.argv[2]
    n2 = int(sys.argv[3])
    match operator:
        case "+":
            print("{} + {} = {}".format(n1, n2, calculator_1.add(n1, n2)))
        case "-":
            print("{} - {} = {}".format(n1, n2, calculator_1.sub(n1, n2)))
        case "/":
            print("{} / {} = {}".format(n1, n2, calculator_1.div(n1, n2)))
        case "*":
            print("{} * {} = {}".format(n1, n2, calculator_1.mul(n1, n2)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
