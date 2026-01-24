import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(5, 5, 7))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(5, 5, 5))

    def test_scalene_triangle(self):
        self.assertFalse(check_isosceles(5, 6, 7))

    def test_degenerate_triangle(self):
        self.assertFalse(check_isosceles(5, 5, 4))

    def test_invalid_input(self):
        self.assertRaises(ValueError, check_isosceles, 5, 'a', 7)
        self.assertRaises(ValueError, check_isosceles, 5, 5, 0)
