#!/usr/bin/env python3
"""
This module constructs a FlyingFish class that inherits from both
a Fish class and a Bird class
"""


class Fish:
    """Represents a fish"""

    def swim(self):
        """Fish swim"""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat"""
        print("The fish lives in water")


class Bird:
    """Represents a bird"""

    def fly(self):
        """Bird flying"""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A fish that can also fly"""

    def fly(self):
        """Flying fish fly"""
        print("The flying fish is soaring!")

    def swim(self):
        """Flying fish swims"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Flying fish habitat"""
        print("The flying fish lives both in water and the sky!")
