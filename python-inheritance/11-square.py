#!/usr/bin/python3
"""Square module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return square description"""
        return "[Square] {}/{}".format(self._Square__size, self._Square__size)

    def area(self):
        """Return area of square"""
        return self._Square__size * self._Square__size
