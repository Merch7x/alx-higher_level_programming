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
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method for width
        setter evals type and value before setting value."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height
        setter evals type and value before setting value."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the ractangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Represents the rectangle with a pound sign"""
        rectangle = []
        if self.__height == 0 or self.__width == 0:
            return ("")

        for i in range(self.__height):
            [rectangle.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
