#!/usr/bin/python
"""Create unittests for max Integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """Define tests for max_integer([..])
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 3, 1]), 4)
        self.assertEqual(max_integer([4, 8, 3]), 8)
        self.assertEqual(max_integer([-4, -3, -1]), -1)
        self.assertEqual(max_integer([1.2, 2.6, 7.6]), 7.6)
        self.assertEqual(max_integer([-4, -1, -3]), -1)
        self.assertEqual(max_integer([-4.0, -3.7, -0.6]), -0.6)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([-4.0]), -4.0)
        self.assertEqual(max_integer("Tit"), 't')
        self.assertEqual(max_integer("Tim"), "m")
        self.assertEqual(max_integer("tim"), "t")
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(
            ["Tim", "is", "always", "right"]), "right")
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
