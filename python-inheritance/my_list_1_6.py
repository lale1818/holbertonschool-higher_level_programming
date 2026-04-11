#!/usr/bin/python3
"""
This module contains the MyList class.
"""


class MyList(list):
    """A subclass of list that provides a sorted printing method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
