#!/usr/bin/python3
""" Deserializes json from a file to Python object"""


import json


def load_from_json_file(filename):
    """Retrieves json from a file and deserializes it
    load stands for load from file
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
