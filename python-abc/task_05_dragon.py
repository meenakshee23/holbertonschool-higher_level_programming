#!/usr/bin/env python3
"""
This module constructs a class Dragon
that inherits from both these mixins
"""


class SwimMixin:
    """Represents SwimMixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Represents FlyMixin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly"""

    def roar(self):
        """Dragon's roar"""
        print("The dragon roars!")
