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

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a subclass"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if not os.pth.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for item in list_cls:
            list_ins.append(cls.create(**item))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            if cls.__name__ == "Rectangle":
                list_keys = ['id', 'width', 'height', 'x', 'y']

            else:
                list_keys = ['id', 'size', 'x', 'y']

            matrix = []
            for csv_elem in csv_list:
                dict_csv = {}
                for kv in enumerate(csv_elem):
                    dict_csv[list_keys[kv[0]]] = int(kv[1])
                matrix.append(dict_csv)

            list_ins = []
            for index in range(len(matrix)):
                list_ins.append(cls.create(**matrix[index]))

            return list_ins
