#!/usr/bin/python3
"""Contains a function that adds two ints or floats
  if the types  are wrong a type error is raised
"""
def add_integer(a, b=98):
  """Adds two ints or floats
  
  Args:
    a (int): an int or float value
    b (int): an in or float value
  """
  if not isinstance(a, (int, float)):
    raise TypeError("a must be an integer")
  
  if not isinstance(b, (int, float)):
    raise TypeError("b must be an integer")
  return (int(a) + int(b))