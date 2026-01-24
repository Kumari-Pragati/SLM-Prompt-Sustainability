import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_perimeter_triangle_positive(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)
        self.assertEqual(perimeter_triangle(6, 8, 10), 24)
        self.assertEqual(perimeter_triangle(10, 20, 30), 60)

    def test_perimeter_triangle_negative(self):
        self.assertRaises(ValueError, perimeter_triangle, -1, 2, 3)
        self.assertRaises(ValueError, perimeter_triangle, 0, 2, 3)
        self.assertRaises(ValueError, perimeter_triangle, 1, 0, 3)
        self.assertRaises(ValueError, perimeter_triangle, 1, 2, 0)
