#!/usr/bin/python3
"""This module returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)"""
    return obj.__dict__
