#!/usr/bin/python3
"""Returns the list of available attributes and methods from an object"""


def lookup(obj):
    """Returns attributes and methods available to object"""
    return dir(obj)
