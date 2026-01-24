import unittest
from mbpp_626_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_positive_number(self):
        """Test that a positive number returns the correct area"""
        self.assertEqual(triangle_area(5), 25)

    def test_zero(self):
        """Test that zero returns zero"""
        self.assertEqual(triangle_area(0), 0)

    def test_negative_number(self):
        """Test that a negative number returns -1"""
        self.assertEqual(triangle_area(-3), -9)

    def test_small_positive_number(self):
        """Test that a small positive number returns a small area"""
        self.assertEqual(triangle_area(0.5), 0.25)

    def test_large_positive_number(self):
        """Test that a large positive number returns a large area"""
        self.assertEqual(triangle_area(100), 10000)
