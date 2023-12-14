import unittest
from models.base import Base


class TestBase(unittest.TestCase):
  """Test the base class from base.py"""
  def test_private_attribute(self):
    """Tests the whether the class attribute is private """
    with self.assertRaises(AttributeError):
      Base.__nb_objects

  def test_class_constructor(self):
    """Test the class constructor instance attribute assignments"""
    obj = Base()
    if obj.id is None:
      self.assertEqual(obj.id, Base.__nb_objects)
    else:
      self.assertIsNotNone(obj.id)

if __name__ == "__main__":
  unittest.main()