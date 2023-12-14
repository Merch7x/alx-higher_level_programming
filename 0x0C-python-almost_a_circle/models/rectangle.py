"""Ctreates a class rectangle"""
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
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.id = super().id

  @property
  def width(self):
    """Gets the value of self and modifys it through a setter"""
    return self.__width
  
  @width.setter
  def width(self, value):
    self.__width = value
  
  @property
  def height(self):
    """Gets the value of self and modifys it through a setter"""
    return self.__height
  
  @height.setter
  def height(self, value):
    self.__height = value
  
  @property
  def x(self):
    """Gets the value of self and modifys it through a setter"""
    return self.__x
  
  @x.setter
  def x(self, value):
    self.__x = value

  @property
  def y(self):
    """Gets the value of self and modifys it through a setter"""
    return self.__y
  
  @y.setter
  def y(self, value):
    self.__y = value