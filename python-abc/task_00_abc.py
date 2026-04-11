#!/usr/bin/python3
"""
Abstrakt Animal klası və onun alt klaslarını (Dog, Cat) ehtiva edən modul.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Bütün heyvanlar üçün abstrakt baza klası."""

    @abstractmethod
    def sound(self):
        """Heyvanın çıxardığı səs üçün abstrakt metod."""
        pass


class Dog(Animal):
    """İti təmsil edən klas."""

    def sound(self):
        """İtin səsini qaytarır."""
        return "Bark"


class Cat(Animal):
    """Pişiyi təmsil edən klas."""

    def sound(self):
        """Pişiyin səsini qaytarır."""
        return "Meow"
