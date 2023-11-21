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

    def area(self):
        """ determines the area of a square"""
        result = self.__size * self.__size
        return result

    @property
    def size(self):
        """ Getter method for size.
        the setter method validates the value to set as size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
