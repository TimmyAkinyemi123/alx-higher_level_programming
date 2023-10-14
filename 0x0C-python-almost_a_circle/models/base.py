#!/usr/bin/python3
"""Defines the class Base"""
import json
import csv
import os.path


class Base:
    """Represents a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances of Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Changes list_dictionaries to JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save instances of subclass to file"""
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())
        else:
            list_dicts = []

        with open(filename, "w") as f:
            f.write(cls.to_join_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Changes JSON string to dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
