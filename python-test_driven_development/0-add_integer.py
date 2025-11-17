#!/usr/bin/python3
"""
This module provides a function that adds two integers
It adds two numbers
The numbers must be int or float
They are cast to int before adding
It returns the sum
"""


def add_integer(a, b=98):
    """
    Add two numbers after validating their types
    Both a and b must be int or float
    Returns the integer sum of the two values
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
