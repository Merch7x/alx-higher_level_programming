#!/usr/bin/python3
"""Contains a class that defines a rectangle"""


class Rectangle:
    """ Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instanciate an object with values

        Args:
            width (int): decribes the width of the rectangle
            height (int): describes the height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @staticmethod
    def RectangleInstances():
        return Rectangle.number_of_instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle with equal width and height

        Args:
            size (int): new height and width
        """
        return (cls(size, size))

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
        res = []
        if self.__height == 0 or self.__width == 0:
            return ("")
        for i in range(self.__height):
            [res.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                res.append("\n")
        return ("".join(res))

    def __repr__(self):
        """Represents the rectangle with a pound sign"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes an instance of the Rectangle"""
        Rectangle.number_of_instances -= 1
        dot = "."
        print("Bye rectangle{}{}{}".format(dot, dot, dot))
