#!/usr/bin/python3
# 2-is_same_class.py

"""Checks the class of an object"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    Args:
        obj (any): The object
        a_class (type): The specified class
    Returns:
        True if obj is an instance of a_class;
        otherwise False.
    """
    return (type(obj) is a_class)
