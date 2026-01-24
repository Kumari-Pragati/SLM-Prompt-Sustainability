import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_perimeter_triangle_typical(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_perimeter_triangle_zero_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 4, 5)

    def test_perimeter_triangle_negative_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(-3, 4, 5)

    def test_perimeter_triangle_non_numeric_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle('a', 4, 5)

    def test_perimeter_triangle_non_integer_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(3.5, 4, 5)

    def test_perimeter_triangle_zero_sides_with_two_non_zero_sides(self):
        self.assertEqual(perimeter_triangle(0, 4, 5), 9)

    def test_perimeter_triangle_zero_sides_with_one_non_zero_sides(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(0, 0, 5)
