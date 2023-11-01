#!/usr/bin/python3

def upper_check(i):
    if 'a' <= i <= 'z':
        return chr(ord(i) - 32)
    else:
        return i


def uppercase(str):
    new_str = ""
    for i in str:
        new_str += upper_check(i)
    print("{}".format(new_str))
