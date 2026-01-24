import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(5, 5, 5))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_scalene_triangle(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_invalid_input_one_side(self):
        self.assertFalse(check_isosceles(5, 5, None))
        self.assertFalse(check_isosceles(5, None, 5))
        self.assertFalse(check_isosceles(None, 5, 5))

    def test_invalid_input_negative_number(self):
        self.assertFalse(check_isosceles(-5, 5, 5))
        self.assertFalse(check_isosceles(5, -5, 5))
        self.assertFalse(check_isosceles(5, 5, -5))
