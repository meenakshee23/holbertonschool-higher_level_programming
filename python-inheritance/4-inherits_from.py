#!/usr/bin/python3
"""
This module defines a function that returns True if the object is an
instance of a class that inherited (directly or indirectly) from it
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
