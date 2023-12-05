#!/usr/bin/python3
"""Creates a subclass of list"""


class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
