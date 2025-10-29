#!/usr/bin/python3
"""This module write a function that returns the JSON representation"""
import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
