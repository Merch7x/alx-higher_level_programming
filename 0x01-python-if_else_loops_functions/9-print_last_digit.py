#!/usr/bin/python3
def print_last_digit(number):
    l_num = (number % 10) if number >= 0 else ((number * -1) % 10)
    print(l_num, end='')
    return l_num
