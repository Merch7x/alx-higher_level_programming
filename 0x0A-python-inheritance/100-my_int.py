#!/usr/bin/python3
"""Use magic methods"""


class MyInt(int):
    """defines a class subclass Myint """
    def __eq__(self, other):
        """Overrides the == operator."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return not super().__ne__(other)
