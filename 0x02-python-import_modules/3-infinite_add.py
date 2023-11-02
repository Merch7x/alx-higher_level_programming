#!/usr/bin/python3
from sys import argv


def add(n):
    return n + 0


if __name__ == "__main__":
    total = 0
    for i in range(len(argv)):
        if i == 0:
            total = 0
        else:
            total += add(int(argv[i]))
    print(total)
