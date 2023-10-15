#!/usr/bin/python3
"""Defines the Square class"""
from model.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"String special method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )

    @property
    def size(self):
        """Gets/Sets the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the instances"""
        if args:
            attr_list = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(arg):
                setattr(Self, attr_list[i], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Saves instances in a dictionary"""
        list_attr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_attr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')

            else:
                dict_res[key] = getattr(Self, key)

        return dict_res
