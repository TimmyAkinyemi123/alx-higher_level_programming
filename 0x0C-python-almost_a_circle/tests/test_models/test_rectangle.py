import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """Test Cases for the rectangle's functionality"""
    @classmethod
    def setUpClass(cls):
        """Sets up __nb_objects for each test case"""
        Base._Base__nb_objects = 0

    def test_init_with_id(self):
        """
        Test initializing with all parameters, including id
        """
        rect = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_init_default(self):
        """
        Test initializing without the id parameter
        """
        rect = Rectangle(8, 15, 2, 2)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)

    def test_invalid_values(self):
        """Test for invalid values"""
        with self.assertRaises(ValueError):
            Rectangle(0, 15, 2, 2)

        with self.assertRaises(ValueError):
            Rectangle(8, -15, 2, 2)

        with self.assertRaises(ValueError):
            Rectangle(8, 15, -2, 2)

    def test_private_attr1(self):
        """
        Test for private attributes
        """
        rect = Rectangle(8, 15, 2, 2)

        with self.assertRaises(AttributeError):
            rect.__width
     
    def test_private_attr2(self):
     """Test for private attributes"""
     rect = Rectangle(8, 15, 2, 2)
     with self.assertRaises(AttributeError):
         rect.__height
     
    def test_private_attr3(self):
     """Test for private attributes"""
     rect = Rectangle(8, 15, 2, 2)
     with self.assertRaises(AttributeError):
         rect.__x

    def test_private_attr4(self):
     """Test for private attributes"""
     rect = Rectangle(8, 15, 2, 2)
     with self.assertRaises(AttributeError):
         rect.__y

    def test_incorrect_attributes(self):
        """Test incorrect amount of attributes"""
        with self.assertRaises(TypeError):
            Rectangle(8, 15, 2, 2, 3, 4, 5)

        with self.assertRaises(TypeError):
            Rectangle()
        
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_invalid_values(self):
        """Test for invalid values"""
        with self.assertRaises(TypeError):
            Rectangle(8, "15", 2, 2)
        
        with self.assertRaises(TypeError):
            Rectangle("8", 15, 2, 2)
        
        with self.assertRaises(TypeError):
            Rectangle(8, 15, "2", 2)
        
        with self.assertRaises(TypeError):
            Rectangle(8, 15, 2, "2")

    def test_instance_of_base(self):
        """
        Test if Rectangle is an instance of Base
        """
        rect = Rectangle(8, 15, 2, 2)
        self.assertIsInstance(rect, Base)
    
    def test_area(self):
        """Test the area method"""
        rect = Rectangle(5, 4)
        self.assertEqual(rect.area(), 20)
        
        rect = Rectangle(8, 6)
        self.assertEqual(rect.area(), 48)
        
        rect = Rectangle(3, 7)
        self.assertEqual(rect.area(), 21)

    def test_display(self):
        """Test the display method"""
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.subTest():
            self.assertEqual(rect.display(), expected_output)

        rect = Rectangle(4, 3, 1, 1)
        expected_output = "\n ####\n ####\n ####\n"
        with self.subTest():
            self.assertEqual(rect.display(), expected_output)
    
    def test_str(self):
        """Test the __str__ method"""
        rect = Rectangle(4, 5, 1, 2, 42)
        expected_output = "[Rectangle] (42) 1/2 - 4/5"
        self.assertEqual(str(rect), expected_output)
        
        rect = Rectangle(7, 3, 0, 0, 99)
        expected_output = "[Rectangle] (99) 0/0 - 7/3"
        self.assertEqual(str(rect), expected_output)
        
        rect = Rectangle(6, 6, 3, 4)
        expected_output = "[Rectangle] (1) 3/4 - 6/6"
        self.assertEqual(str(rect), expected_output)
    
    def test_update_with_args(self):
        """Test the update method with *args"""
        rect = Rectangle(5, 5)
        rect.update(1, 10, 20, 30, 40)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 30)
        self.assertEqual(rect.y, 40)
        
        rect.update(2, 8)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 30)
        self.assertEqual(rect.y, 40)
    
    def test_update_with_kwargs(self):
        """Test the update method with **kwargs"""
        rect = Rectangle(5, 5)
        rect.update(1, width=10, y=40)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 40)
    
    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rect.to_dictionary(), expected_dict)
        
        rect2 = Rectangle(7, 7, 0, 0, 2)
        expected_dict2 = {'id': 2, 'width': 7, 'height': 7, 'x': 0, 'y': 0}
        self.assertEqual(rect2.to_dictionary(), expected_dict2)