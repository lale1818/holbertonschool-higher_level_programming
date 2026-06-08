#!/usr/bin/python3
"""Defines a class Square with a print method"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the square"""
        self.size = size

    @property
    def size(self):
        """Getter to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to validate and set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
