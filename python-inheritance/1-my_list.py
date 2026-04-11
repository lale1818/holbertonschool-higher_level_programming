#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """A subclass of list with additional sorting functionality."""

    def print_sorted(self):
        """
        Prints the list in ascending order.
        Assumes all elements in the list are integers.
        """
        print(sorted(self))
