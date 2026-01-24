import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(6, 8, 10), 24)

    def test_zero(self):
        self.assertRaises(ValueError, perimeter_triangle, 0, 4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 0, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 4, 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter_triangle, -3, 4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, -4, 5)
        self.assertRaises(ValueError, perimeter_triangle, 3, 4, -5)

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, perimeter_triangle, 'a', 4, 5)
        self.assertRaises(TypeError, perimeter_triangle, 3, 'b', 5)
        self.assertRaises(TypeError, perimeter_triangle, 3, 4, 'c')
