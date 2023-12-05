#!/usr/bin/python3
"""Creates an empty class"""


class BaseGeometry:
    """ An empty class"""
    def area(self):
        """A public method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than or equal to zero
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        return value


class Rectangle(BaseGeometry):
    """ A subclass of Basegeometry"""

    def __init__(self, width, height):
        """Initialises objects of the class
        Args:
            width (int) - width of rectangle
            height (int) - height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
