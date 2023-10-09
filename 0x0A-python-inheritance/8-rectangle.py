#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """Represent base geometry."""

    def __init__(self, width, height):
        """Instantiates a Rectangle with width and height.
        Args:
           width (int): width of the rectangle
           height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
