#!/usr/bin/python3
"""
Bu modul list-dən miras alan MyList klasını təqdim edir.
"""


class MyList(list):
    """Standart list klasını genişləndirən klas."""

    def print_sorted(self):
        """Siyahını artan sıra ilə (sorted) çap edir."""
        print(sorted(self))
