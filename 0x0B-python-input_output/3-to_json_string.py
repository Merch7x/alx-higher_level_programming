#!/usr/bin/python3
"""Returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """ encode object to json"""
    data = json.dumps(my_obj)
    return data
