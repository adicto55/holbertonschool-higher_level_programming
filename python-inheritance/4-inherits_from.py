#!/usr/bin/python3
"""Module for checking if object is inherited from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is inherited from a_class, False otherwise."""
    return isinstance(obj, a_class) and type(obj) is not a_class
