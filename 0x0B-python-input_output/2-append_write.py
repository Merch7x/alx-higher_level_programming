#!/usr/bin/python3
"""Append to file"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        data = f.write(text)
        return data
