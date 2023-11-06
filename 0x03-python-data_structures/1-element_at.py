#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 | idx > len(my_list):
        return None
    for x in my_list:
        if x == my_list[idx]:
            return x
