#!/usr/bin/python3
"""Module that defines MyList"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print sorted list and return a new sorted list"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
        return new_list
