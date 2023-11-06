#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    new_string = [x for x in new_string if x != 'C' and x != 'c']
    return "".join(new_string)
