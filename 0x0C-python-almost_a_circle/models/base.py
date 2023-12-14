#!/usr/bin/python3
"""Creates a base class"""


class Base():
  """A base class"""
  __nb_objects = 0
  def __init__(self, id=None):
    """Instanciate a class object
    
    Args:
      id: a form of object id
    """
    if id is None:
      Base.__nb_objects += 1
      self.id = Base.__nb_objects
    else:
      self.id = id

