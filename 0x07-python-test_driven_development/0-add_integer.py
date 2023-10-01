#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """Adds 2 integers
    a and b must be first casted to integers if they are float.

    Raises:
        TypeError: if any of the arguments are non-integer and non-float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
