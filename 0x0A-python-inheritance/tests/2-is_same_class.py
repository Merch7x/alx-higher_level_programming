#!/usr/bin/python3
""" Checks for the equality of objects"""


def is_same_class(obj, a_class):
    """ checks whether an obj is a memeber of a specified class

    Args:
        obj - an instnace of a class
        a_class - a class ref
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
