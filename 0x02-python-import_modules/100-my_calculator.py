#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def operator_to_use(operator):
    match operator:
        case '+':
            return add
        case '-':
            return sub
        case '*':
            return mul
        case '/':
            return div
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = operator_to_use(sys.argv[2])
    result = operator(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
