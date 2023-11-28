#!/usr/bin/python3
""" Create a locked class"""


class LockedClass:
    """
    Instantiate a class only if it called firstname
    this is done through creation of a lockedclass
    """
    __slots__ = ["first_name"]
