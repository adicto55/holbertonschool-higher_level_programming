#!/usr/bin/python3
"""Module for checking if object is exactly instance of a class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly instance of a_class."""
    return type(obj) is a_class
