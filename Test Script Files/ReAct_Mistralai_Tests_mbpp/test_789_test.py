import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_positive_numbers(self):
        """Test perimeter calculation with positive numbers"""
        self.assertEqual(perimeter_polygon(5, 3), 15)
        self.assertEqual(perimeter_polygon(10, 2), 20)

    def test_zero_side_length(self):
        """Test perimeter calculation with zero side length"""
        with self.assertRaises(ValueError):
            perimeter_polygon(5, 0)

    def test_negative_side_length(self):
        """Test perimeter calculation with negative side length"""
        with self.assertRaises(ValueError):
            perimeter_polygon(5, -3)

    def test_zero_sides(self):
        """Test perimeter calculation with zero sides"""
        with self.assertRaises(ValueError):
            perimeter_polygon(0, 3)

    def test_float_side_length(self):
        """Test perimeter calculation with float side length"""
        self.assertAlmostEqual(perimeter_polygon(5, 3.14), 15.39)

    def test_large_sides(self):
        """Test perimeter calculation with large sides"""
        self.assertEqual(perimeter_polygon(1000000, 1), 1000000)
