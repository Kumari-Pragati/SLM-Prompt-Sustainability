import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_perimeter_triangle_valid(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_perimeter_triangle_negative(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(-3, 4, 5)

    def test_perimeter_triangle_non_numeric(self):
        with self.assertRaises(TypeError):
            perimeter_triangle('a', 4, 5)

    def test_perimeter_triangle_zero(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)

    def test_perimeter_triangle_zero_and_non_zero(self):
        self.assertEqual(perimeter_triangle(0, 4, 5), 9)

    def test_perimeter_triangle_non_zero_and_zero(self):
        self.assertEqual(perimeter_triangle(4, 0, 5), 9)

    def test_perimeter_triangle_all_zero(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)
