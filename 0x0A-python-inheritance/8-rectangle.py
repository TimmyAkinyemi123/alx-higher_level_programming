#!/usr/bin/python3

"""Defines a Rectangle that inherits from Basegeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle using Basegeometry."""

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
