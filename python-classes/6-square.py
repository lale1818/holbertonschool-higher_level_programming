#!/usr/bin/python3
"""Defines a class Square with size and position coordinates"""


class Square:
    """Represents a square with coordinates"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with comprehensive validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square taking position into account"""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan buraxılacaq boş sətirlər
        for _ in range(self.__position[1]):
            print("")

        # Kvadratın özünün və sol boşluqlarının çapı
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
