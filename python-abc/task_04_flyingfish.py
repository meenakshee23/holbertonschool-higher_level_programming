#!/usr/bin/python3
"""This module defines a FlyingFish class that inherits from Fish and Bird."""


class Fish:
    """Represents a Fish."""

    def swim(self):
        """Prints a message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message."""
        print("The fish lives in water")


class Bird:
    """Represents a Bird."""
    def fly(self):
        """Prints a message."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a FlyingFish inheriting from Fish and Bird."""

    def fly(self):
        """Prints a message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message."""
        print("The flying fish lives both in water and the sky!")
