#!/usr/bin/python3
"""
Bu modul Miksinlərin (Mixins) istifadəsini nümayiş etdirir.
"""


class SwimMixin:
    """Üzmə bacarığı verən miksin."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Uçma bacarığı verən miksin."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    SwimMixin və FlyMixin-dən miras alan Dragon klası.
    Hər iki bacarığı birləşdirir.
    """
    def roar(self):
        print("The dragon roars!")
