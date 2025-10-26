#!/usr/bin/python3
"""This module defines the VerboseList class"""


class VerboseList(list):
    """Class that extends the Python list with notifications."""

    def append(self, item):
        """After adding the item to the list, print a message"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """After extending the list, print a message"""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Before removing the item from the list, print a message"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Before popping the item from the list, print a message"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
