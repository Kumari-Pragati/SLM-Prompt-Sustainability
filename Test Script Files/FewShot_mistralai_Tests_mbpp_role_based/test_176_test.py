import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(6, 8, 10), 24)

    def test_zero(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter_triangle, -3, -4, -5)

    def test_two_equal_sides(self):
        self.assertEqual(perimeter_triangle(3, 3, 4), 10)

    def test_one_zero_side(self):
        self.assertRaises(ValueError, perimeter_triangle, 3, 0, 4)
