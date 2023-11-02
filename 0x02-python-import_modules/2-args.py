#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argument = "arguments" if len(argv) == 1 or len(argv) > 2 else "argument"
    if len(argv) == 1:
        print("0 {}.".format(argument))
    elif len(argv) >= 2:
        print("{} {}:".format(len(argv) - 1, argument))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
