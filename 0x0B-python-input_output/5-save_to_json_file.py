#!/usr/bin/python3
"""Save Json represented object to file"""


import json


def save_to_json_file(my_obj, filename):
    """saves a json represented object to a file

    Args:
        my_object (str): object to serialize
        filename (str): file to write to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
