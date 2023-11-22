#!/usr/bin/python3

""" Defines a class square """


class Square:
    """ Defines a class square """

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ constructor docstring
        Args:
            size: Size of the square.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """ determines the area of a square"""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """ print square as bangs """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

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
        else:
            self.__size = value

    @property
    def position(self):
        """ Get the value of position and set it """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance (value, tuple) or 
            not all(isinstance(x, int) for x in value) or
            not all(x >= 0 for x in value) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
