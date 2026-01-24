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

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            perimeter_triangle("a", 2, 3)

    def test_non_numeric_input_2(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1, "b", 3)

    def test_non_numeric_input_3(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2, "c")

    def test_non_numeric_input_4(self):
        with self.assertRaises(TypeError):
            perimeter_triangle("a", "b", "c")

    def test_non_numeric_input_5(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1.5, 2, 3)

    def test_non_numeric_input_6(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2.5, 3)

    def test_non_numeric_input_7(self):
        with self.assertRaises(TypeError):
            perimeter_triangle(1, 2, 3.5)

    def test_non_numeric_input_8(self):
        with self.assertRaises(TypeError):
            perimeter_triangle("a", "b", "c")
