#!/usr/bin/python3
"""Sees if the object is an instance of a class that inherited from it"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherits from it"""
    return isinstance(obj, a_class)
