#!/usr/bin/python3
"""Module that defines MyList"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print list in ascending order and return a new sorted list"""
        new_list = sorted(self)
        print(new_list)
        return new_list
