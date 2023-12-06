#!/usr/bin/python3
import json
"""Returns the JSON representation of an object"""


def to_json_string(my_obj):
    """ encode object to json"""
    data = json.dumps(my_obj)
    return data
