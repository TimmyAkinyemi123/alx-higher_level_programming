#!/usr/bin/python3
# 4-inherits_from.py

"""Checks if object is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of an
    inherited class.

    Args:
        obj (any): The object
        a_class (type): class
    Returns:
        True if obj is an instance of a_class;
        otherwise False
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
