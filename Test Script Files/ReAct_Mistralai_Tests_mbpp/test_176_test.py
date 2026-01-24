import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_positive_numbers(self):
        """Test perimeter with positive numbers"""
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(6, 8, 10), 24)

    def test_zero(self):
        """Test perimeter with zero"""
        self.assertRaises(ValueError, perimeter_triangle, 0, 4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 0, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 4, 0)

    def test_negative_numbers(self):
        """Test perimeter with negative numbers"""
        self.assertRaises(ValueError, perimeter_triangle, -3, 4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, -4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 4, -5)

    def test_one_negative_two_positive(self):
        """Test perimeter with one negative and two positive numbers"""
        self.assertRaises(ValueError, perimeter_triangle, -3, 4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, -4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 4, -5)

    def test_two_negative_one_positive(self):
        """Test perimeter with two negative and one positive number"""
        self.assertRaises(ValueError, perimeter_triangle, -3, -4, 5)
        self.assertRaises(ValueError, perimeter_triangle, -3, 4, -5)
        self.assertRaises(ValueError, perimeter_triangle, 3, -4, -5)

    def test_two_equal_numbers(self):
        """Test perimeter with two equal numbers"""
        self.assertEqual(perimeter_triangle(3, 3, 4), 10)
        self.assertRaises(ValueError, perimeter_triangle, 0, 0, 0)

    def test_one_equal_two_zero(self):
        """Test perimeter with one equal and two zero numbers"""
        self.assertRaises(ValueError, perimeter_triangle, 3, 0, 0)
        self.assertRaises(ValueError, perimeter_triangle, 0, 3, 0)
        self.assertRaises(ValueError, perimeter_triangle, 0, 0, 3)
