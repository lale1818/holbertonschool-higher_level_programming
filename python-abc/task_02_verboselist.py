#!/usr/bin/python3
"""
This module defines the VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification."""
        items_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """Removes an item and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
