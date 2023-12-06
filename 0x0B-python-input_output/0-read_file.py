#!/usr/bin/python3
""" Reads from a text file and prints it to stdout"""


def read_file(filename=""):
    """ opens a file and reads the contents of the entire file"""
    with open(filename, 'r') as f:
        data = f.read()
        print(data)
