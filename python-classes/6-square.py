#!/usr/bin/python3
"""Defines a class Square with strict size and position validation"""


class Square:
    """Represents a square with size and position coordinate logic"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter to retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to validate and set the private size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter to retrieve the private position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to strictly validate and set the private position tuple"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' with horizontal and vertical spacing"""
        if self.__size == 0:
            print("")
            return

        # Yuxarı boşluqlar (Yalnız size > 0 olduqda)
        for _ in range(self.__position[1]):
            print("")

        # Sol boşluqlar və kvadratın sətirləri
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
