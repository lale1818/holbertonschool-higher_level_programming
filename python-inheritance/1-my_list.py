#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList inherits from list and provides a sorted print method.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        """
        print(sorted(self))
