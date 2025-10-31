#!/usr/bin/python3
"""This module creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Loads a json file"""
    with open(filename, 'r') as file:
        return json.load(file)
