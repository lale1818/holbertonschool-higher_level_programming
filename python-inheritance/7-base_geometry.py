#!/usr/bin/python3
"""
BaseGeometry klasını ehtiva edən modul.
"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza klası."""

    def area(self):
        """Sahəni hesablayan metod."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyərin mütləq tam ədəd (və Boolean olmayan) 
        və müsbət olduğunu yoxlayır.
        """
        # Diqqət: type(value) is int - Boolean-ları (True/False) bloklayır
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
