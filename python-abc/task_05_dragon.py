#!/usr/bin/python3
"""Constructs a class Dragon that inherits from both these mixins"""


class SwimMixin:

    def swim(self):
        """Prints a message"""
        print("The creature swims!")


class FlyMixin:

    def fly(self):
        """Prints a message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        """Prints a message"""
        print("The dragon roars!")
