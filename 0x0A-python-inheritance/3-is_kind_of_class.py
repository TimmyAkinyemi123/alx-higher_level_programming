#!/usr/bin/python3
# 3-is_kind_of_class.py

"""Checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class
    or a subclass of a_class.
    Args:
        obj (any): The object
        a_class: class or subclass
    Returns:
        True if obj is an instance of a_class or subclass;
        otherwise False
    """
    return (isinstance(obj, a_class))
