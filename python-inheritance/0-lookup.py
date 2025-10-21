#!/usr/bin/python3
"""This module writes a function that returns the list of available attributes"""


def lookup(obj):
    """Returns the list object"""
    return dir(obj)
