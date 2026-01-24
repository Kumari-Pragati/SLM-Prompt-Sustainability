import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_zero_sides(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)

    def test_negative_sides(self):
        with self.assertRaises(Exception):
            perimeter_triangle(-1, -2, -3)

    def test_large_numbers(self):
        self.assertEqual(perimeter_triangle(10000, 10000, 10000), 30000)

    def test_equal_sides(self):
        self.assertEqual(perimeter_triangle(5, 5, 5), 15)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            perimeter_triangle("a", 2, 3)
