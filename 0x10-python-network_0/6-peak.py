#!/usr/bin/python3
"""Sorts a list of intgers to find
largest
"""


def find_peak(list_of_integrs):
    """Sorts a list"""
    if list_of_integrs:
        list_of_integrs.sort(reverse=True)
        return list_of_integrs[0]
    else:
        return None
