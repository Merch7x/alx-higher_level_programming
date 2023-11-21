#!/usr/bin/python3

""" Defines a class square """


class Square:
    """ Defines a class square """
    def __init__(self, size=0):
        """ __init__ constructor docstring
        Args:
            size: Size of the square.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
