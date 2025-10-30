#!/usr/bin/python3
"""This module returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns an object"""
    return json.loads(my_str)
