#!/usr/bin/python3
"""Defines test cases for Base class"""
import unittest
from unittest import TestCase
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


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

    def test_list_of_dictionaries(self):
        """Tests to_json_string method with
        list of dicts"""
        list_dicts = [
                {'name': 'John', 'age': 30},
                {'name': 'Alice', 'age': 25}
                ]
        result = Base.to_json_string(list_dicts)
        expected = (
                '[{"name": "John", "age": 30},'
                '{"name": "Alice", "age": 25}]'
                )
        self.assertEqual(result, expected)

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method."""
        r1 = Rectangle(3, 5)
        r2 = Rectangle(7, 2)
        with self.subTest():
            with self.assertRaises(FileNotFoundError):
                Rectangle.save_to_file_csv([r1, r2])
        s1 = Square(4)
        s2 = Square(2, 1, 2)
        with self.subTest():
            with self.assertRaises(FileNotFoundError):
                Square.save_to_file_csv([s1, s2])

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method."""
        with self.subTest():
            with self.assertRaises(FileNotFoundError):
                Rectangle.load_from_file_csv()

        with self.subTest():
            with self.assertRaises(FileNotFoundError):
                Square.load_from_file_csv()

    def test_create(self):
        """Test create method."""
        r1 = Rectangle(3, 5)
        r2 = Rectangle(7, 2)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        r1_copy = Rectangle.create(**r1_dict)
        r2_copy = Rectangle.create(**r2_dict)
        self.assertEqual(r1, r1_copy)
        self.assertEqual(r2, r2_copy)

        s1 = Square(4)
        s2 = Square(2, 1, 2)
        s1_dict = s1.to_dictionary()
        s2_dict = s2.to_dictionary()
        s1_copy = Square.create(**s1_dict)
        s2_copy = Square.create(**s2_dict)
        self.assertEqual(s1, s1_copy)
        self.assertEqual(s2, s2_copy)

    def test_load_from_file(self):
        """Test load_from_file method."""
        r1 = Rectangle(3, 5)
        r2 = Rectangle(7, 2)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        r1_copy = Rectangle.load_from_file()
        r2_copy = Rectangle.load_from_file()
        self.assertEqual(r1, r1_copy[0])
        self.assertEqual(r2, r2_copy[1])

        s1 = Square(4)
        s2 = Square(2, 1, 2)
        s1_dict = s1.to_dictionary()
        s2_dict = s2.to_dictionary()
        s1_copy = Square.load_from_file()
        s2_copy = Square.load_from_file()
        self.assertEqual(s1, s1_copy[0])
        self.assertEqual(s2, s2_copy[1])
