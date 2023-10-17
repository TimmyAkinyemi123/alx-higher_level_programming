#!/usr/bin/python3
"""Defines test cases for Base class"""
import unittest
import os
from unittest import TestCase
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """Tests the Base class functionalities"""
    def setUp(self):
        """Sets up nb_objects for every test"""
        Base._Base__nb_objects = 0

    def test_nb_increment(self):
        """tests the increment of __nb_objects"""
        instance_1 = Base()
        instance_2 = Base()
        instance_3 = Base()
        self.assertEqual(instance_1.id, 1)
        self.assertEqual(instance_2.id, 2)
        self.assertEqual(instance_3.id, 3)

    def test_base_private_attr(self):
        """Tests if __nb_objects is private"""
        with self.assertRaises(AttributeError):
            b = Base(10)
            nb_objects = b.__nb_objects

    def test_id(self):
        """Tests the id assignment"""
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_default_id(self):
        """Tests default id (None)"""
        instance_1 = Base()
        instance_2 = Base()
        self.assertEqual(instance_1.id, 1)
        self.assertEqual(instance_2.id, 2)

    def test_mixed_id(self):
        """Test mixed cases"""
        instance_1 = Base()
        instance_2 = Base(10)
        instance_3 = Base()
        instance_4 = Base(20)
        self.assertEqual(instance_1.id, 1)
        self.assertEqual(instance_2.id, 10)
        self.assertEqual(instance_3.id, 2)
        self.assertEqual(instance_4.id, 20)

    def test_string_id(self):
        """ Test string id """
        new = Base('7')
        self.assertEqual(new.id, '7')

    def test_multiple_id_arguments(self):
        """Test cases of multiple arguments"""
        with self.assertRaises(TypeError):
            base_instance = Base(5, 10)

    def test_empty_list(self):
        """Test to_json_string method with
        empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_none_input(self):
        """Tests to_json_string with no input"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_save_to_file_1(self):
        """ Tests the save_to_file method """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Tests the save_to_file method """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    if __name__ == "__main__":
        unittest.main()
