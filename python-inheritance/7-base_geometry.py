#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class that defines basic geometry properties and methods.
    """

    def area(self):
        """
        Public instance method that calculates the area.
        Raises an Exception because it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an input value as a positive integer.

        Args:
            name (str): The name of the variable.
            value (int): The value to be validated.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
