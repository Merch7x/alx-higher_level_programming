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
        obj = Rectangle(height=15, width=9, x=7, y=9, id=None)
        self.assertIsInstance(obj, Rectangle)

    def test_typeError(self):
        """Test type of the attributes"""
        with self.assertRaises(TypeError):
            obj = Rectangle(height="hi", width=7)
        with self.assertRaises(TypeError):
            obj = Rectangle(height=8, width="jik")
        with self.assertRaises(TypeError):
            obj = Rectangle(height=15, width=10, x="it", y=2)
        with self.assertRaises(TypeError):
            obj = Rectangle(height=20, width=10, x=5, y="it")
    
    def test_valueError_width_height(self):
        """Test value of width and height"""
        with self.assertRaises(ValueError):
            obj = Rectangle(height=0, width=5)
        with self.assertRaises(ValueError):
            obj = Rectangle(height=20, width=0)
        with self.assertRaises(ValueError):
            obj = Rectangle(height=-5, width=10)
        with self.assertRaises(ValueError):
            obj = Rectangle(height=20, width=-6)
    
    def test_x_y_valueError(self):
        """Test value of x and y"""
        with self.assertRaises(ValueError):
            obj = Rectangle(height=20, width=10, x=-1, y=6)
        with self.assertRaises(ValueError):
            obj = Rectangle(height=20, width=10, x=7, y=-4)


