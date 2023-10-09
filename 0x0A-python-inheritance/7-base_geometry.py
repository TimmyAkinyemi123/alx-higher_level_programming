#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates value
        Raises:
           TypeError: if value is not an integer
           ValueError: if value is less than or equal to 0"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
      