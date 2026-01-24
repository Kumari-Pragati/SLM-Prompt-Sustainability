import unittest
from mbpp_176_code import perimeter_triangle

class TestPerimeterTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)

    def test_zero_sides(self):
        self.assertEqual(perimeter_triangle(0, 0, 0), 0)

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter_triangle(-1, 2, 3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            perimeter_triangle('a', 2, 3)

    def test_non_numeric_input_2(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 'b', 3)

    def test_non_numeric_input_3(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2, 'c')

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter_triangle(1, 2, 5)
