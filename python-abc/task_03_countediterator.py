#!/usr/bin/python3
"""
Bu modul iteratorun neçə element keçdiyini sayan 
CountedIterator klasını təqdim edir.
"""


class CountedIterator:
    """İterasiya olunmuş elementlərin sayını izləyən iterator klası."""

    def __init__(self, iterable):
        """Iteratoru və sayğacı inisializasiya edir."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """İndiyə qədər keçilmiş elementlərin sayını qaytarır."""
        return self.count

    def __next__(self):
        """Növbəti elementi qaytarır və sayğacı artırır."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
