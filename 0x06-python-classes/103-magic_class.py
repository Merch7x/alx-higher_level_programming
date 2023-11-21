#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode."""

import math


class MagicClass:
    """Defines a circle."""

    def __init__(self, radius=0):
        """Initialiaze values.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns The circumference."""
        return (2 * math.pi * self.__radius)
