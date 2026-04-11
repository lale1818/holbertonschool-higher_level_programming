#!/usr/bin/python3
"""Module MyList"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Print list in ascending sorted order"""
        print(sorted(self))
