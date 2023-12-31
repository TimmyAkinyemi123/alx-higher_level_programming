#!/usr/bin/python3
# 4-rectangle.py

""" Defines a class Rectangle. """


class Rectangle:
    """Creates a new rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle
        Args:
            width(int): width of the new rectangle
            height(int): height of the new rectangle
        Attributes:
            number_of_instances(int): number of Rectangle instances
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Gets or sets the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets or sets the width """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a printable rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                rec.append("#")
            if i != self.__height - 1:
                rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        """Returns the string representation of the Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Print a message after deletion of a Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
