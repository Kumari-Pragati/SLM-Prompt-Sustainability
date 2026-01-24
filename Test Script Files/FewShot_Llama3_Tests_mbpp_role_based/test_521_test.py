import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 4))

    def test_non_isosceles_triangle(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_degenerate_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_isosceles('a', 'b', 'c')

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            check_isosceles(-1, -1, -1)
