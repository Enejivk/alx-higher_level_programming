#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    try:
        n1 = int(argv[1])
        operator = argv[2]
        n2 = int(argv[3])
    except ValueError:
        print("Error: Please provide valid integer numbers.")
        exit(1)

    result = None
    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = sub(n1, n2)
    elif operator == "*":
        result = mul(n1, n2)
    elif operator == "/":
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
            exit(1)
        result = div(n1, n2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(n1, operator, n2, result))
