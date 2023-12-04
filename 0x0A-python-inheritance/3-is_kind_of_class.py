#!/usr/bin/python3
""" Check for equality of classes"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of or if
    the object is an instance of a class that inherited
    from a specified class

    Args:
        obj - class instance
        a_class - a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
