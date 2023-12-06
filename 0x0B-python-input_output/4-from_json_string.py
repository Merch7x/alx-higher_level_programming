#!/usr/bin/python3
"""Deserialization from json to python object"""


import json


def from_json_string(my_str):
    """change json to python object"""

    data = json.loads(my_str)
    return data
