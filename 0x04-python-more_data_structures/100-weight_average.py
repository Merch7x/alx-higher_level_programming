#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    avr = 0
    if not my_list:
        return 0
    for tupple in my_list:
        num += tupple[0] * tupple[1]
        avr += tupple[1]

    return (num / avr)
