import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):
    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_perimeter_zero_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 0)

    def test_perimeter_negative_sides(self):
        self.assertEqual(perimeter_triangle(-3, 4, 5), 6)

    def test_perimeter_non_numeric_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle('a', 4, 5)

    def test_perimeter_mixed_sides(self):
        self.assertEqual(perimeter_triangle(3, 4, -5), 7)

    def test_perimeter_zero_sides_with_negative(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, -5)
