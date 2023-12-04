#!/usr/bin/python3
"""Add attributes to an object"""


def add_attribute(obj, attribute_name, attribute_value):
    """Adds a new attribute to an object if possible,
    raises TypeError Otherwise.

    Args:
        obj: The object to which the attribute should be added.
        attribute_name: The name of the attribute.
        attribute_value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute_name] = attribute_value
