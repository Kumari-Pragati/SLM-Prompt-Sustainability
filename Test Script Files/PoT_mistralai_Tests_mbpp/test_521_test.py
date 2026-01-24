import unittest
from mbpp_521_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(5, 5, 6))
        self.assertTrue(check_isosceles(3, 3, 4))

    def test_scalene_triangle(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_equilateral_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_degenerate_triangle(self):
        self.assertFalse(check_isosceles(0, 0, 0))
        self.assertFalse(check_isosceles(1, 1, 0))
        self.assertFalse(check_isosceles(1, 0, 1))
