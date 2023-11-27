#!/usr/bin/python3
"""Contains a class that defines a rectangle"""


class Rectangle:
    """ Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instanciate an object with values

        Args:
            width (int): decribes the width of the rectangle
            height (int): describes the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ gettaer method for width
        setter evals type and value before setting value"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height
        setter evals type and value before setting value"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
