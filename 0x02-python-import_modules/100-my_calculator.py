#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
    operator = sys.argv[2]
    if operator not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    from calculator_1 import add, sub, mul, div

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if operator == "/":
        print("{:d} * {:d} = {:d}".format(a, b, div(a, b)))
