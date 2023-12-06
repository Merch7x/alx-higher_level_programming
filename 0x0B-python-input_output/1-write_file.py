#!/usr/bin/python3
"""Writes a string to a textfile"""


def write_file(filename="", text=""):
    """write a string to a file

    Args:
        filename (str) - name of file
        text (str) - str to be written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        data = f.write(text)
        print(data)
