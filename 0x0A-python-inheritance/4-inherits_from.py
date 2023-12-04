#!/usr/bin/python3
""" Check for subclasses """


def inherits_from(obj, a_class):
    """returns true if the obj is a direct or indirect instance
    of a_class

    Args:
        obj - instance of  a class
        a_class - a class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
