#!/usr/bin/python3
"""encode a class instnace to json"""


import json


def class_to_json(obj):
    """serialize a class instance object to json

    Args:
        obj (class): an instance of a class
    """
    return obj.__dict__
