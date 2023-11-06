#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 | idx > len(my_list) - 1:
        return None
    for x in my_list:
        if x == my_list[idx]:
            return my_list[idx]
