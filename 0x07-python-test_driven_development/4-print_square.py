#!/usr/bin/python3
"""Create a function that prints a square"""


def print_square(size):
    """prints a square as the symbol # 

    Args:
      size (int): size of the square
    Raises:
      TypeError: if size is not an int
      ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    square = []
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
