#!/usr/bin/env python3
"""VerboseList that extends the Python list class"""

class VerboseList(list):
    """A list that prints notifications when modified"""

    def append(self, item):
        """Add the item and print a message"""
        super().append(item)
        print(f"Added [item] to the list.")

    def extend(self, iterable):
        """Extend the list and print a message"""
        super().extend(iterable)
        print(f"Extended the list with [x] items.")

    def remove(self, item):
        """Remove an item and print a message"""
        print(f"Removed [item] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a message"""
        item = self[index]
        print(f"Popped [item] from the list.")
        return super().pop(index)
