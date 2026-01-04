#!/usr/bin/python3
"""Module for checking if object is instance of or inherited from a class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of or inherited from a_class."""
    return isinstance(obj, a_class)
