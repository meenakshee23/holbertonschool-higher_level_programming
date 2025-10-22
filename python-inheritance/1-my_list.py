#!/usr/bin/python3
"""This module defines a class MyList that inherits from list"""


class MyList(list):
    """Write a class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
