#!/usr/bin/python3
"""Creates a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Creates a representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle object instanciation

        Args:
          width (int): width of rectangle
          height (int): height of rectangle
          x (int)
          y (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the value of self and modifys it through a setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value of self and modifys it through a setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value of self and modifys it through a setter"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the value of self and modifys it through a setter"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """display the area of rectangle as #"""
        rectangle = []
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        "Return the print and str representation of the rectangle"
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
