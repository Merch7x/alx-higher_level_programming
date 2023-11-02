#!/usr/bin/python3
from re import match
import hidden_4

if __name__ == "__main__":
    original = dir(hidden_4)
    new = [item for item in original if not match(r'^__', item)]
    print("{}\n{}\n{}".format(*new))
