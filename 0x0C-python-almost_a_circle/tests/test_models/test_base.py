#!/usr/bin/python3
"""Defines test cases for Base class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.testCase):
    """Tests the Base class functionalities"""
    def setUp(self):
        """Sets up nb_objects for every test"""
        Base._Base__nb_objects = 0

    def test_nb_increment(self):
        """tests the increment of __nb_objects"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertEqual(Base.__nb_objects, 3)

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
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 10)
        self.assertEqual(base_instance3.id, 11)
        self.assertEqual(base_instance4.id, 20)

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
        list_dicts = [{'name': 'John', 'age': 30},
                {'name': 'Alice', 'age': 25}]
        result = Base.to_json_string(list_dicts)
        expected = '[{"name": "John", "age": 30},
        {"name": "Alice", "age": 25}]'
        self.assertEqual(result, expected)

ngle.json")

                                    def test_save_to_file_empty_list(self):
                                                Rectangle.save_to_file([])
                                                        self.assertFalse(os.path.exists("Rectangle.json"))

                                                            def test_save_to_file_with_rectangles(self):
                                                                        r1 = Rectangle(10, 7, 2, 8)
                                                                                r2 = Rectangle(2, 4)
                                                                                        Rectangle.save_to_file([r1, r2])
                                                                                                self.assertTrue(os.path.exists("Rectangle.json"))

                                                                                                    def tearDown(self):
                                                                                                                if os.path.exists("Rectangle.json"):
                                                                                                                                os.remove("Rectangle.json")





