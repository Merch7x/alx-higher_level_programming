import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Define tests for a Superclass rectangle that inherits from Base"""
    def test_constructor_height_weight(self):
        """Test object creation with width and height"""
        obj = Rectangle(height=10, width=5)
        self.assertIsInstance(obj, Rectangle)

    def test_constructor_default_vars(self):
        """Test object creation for default vars"""
        obj = Rectangle(height=10, width=5, x=7, y=8)
        self.assertIsInstance(obj, Rectangle)
    
    def test_constructor_superclass_id(self):
        """Test object creation of an attribute from a superclass"""
        obj = Rectangle(height=15, width=9, x=7, y=9, id=22)
        self.assertIsInstance(obj, Rectangle)

