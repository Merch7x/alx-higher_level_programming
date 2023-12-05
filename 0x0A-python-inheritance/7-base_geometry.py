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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
