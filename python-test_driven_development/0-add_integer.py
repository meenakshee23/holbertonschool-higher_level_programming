#!/usr/bin/python3
"""
This module defines a function that adds two integers.
The numbers must be integers or floats.
Floats are cast to integers before addition.
The function returns the sum of the two numbers.
No imports are required.
"""


def add_integer(a, b=98):
    """
    Adds two integers after type validation.
    Floats are cast to integers before addition.
    Returns the sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
