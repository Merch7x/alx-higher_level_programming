#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    remove = []
    for k, v in a_dictionary.items():
        if v == value:
            remove.append(k)
    for k in remove:
        a_dictionary.pop(k)
    return a_dictionary
