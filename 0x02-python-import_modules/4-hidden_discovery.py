#!/usr/bin/python3
from re import match

if __name__ == "__main__":
    import hidden_4
    original = dir(hidden_4)
    new = [item for item in original if not match(r'^__', item)]
    print("{}\n{}\n{}".format(*new))
