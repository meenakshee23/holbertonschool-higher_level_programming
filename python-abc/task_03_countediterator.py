#!/usr/bin/python3
"""This module defines the CountedIterator class"""


class CountedIterator:
    """Represents a class CountedIterator"""

    def __init__(self, iterable):
        """Initializes the iterator object and the counter"""
        self.iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        """Return the next item and increment the counter"""
        item = next(self.iterator)
        self._count += 1
        return item

    def get_count(self):
        """Iterate over items using a loop or manual calls"""
        return self.get_count
