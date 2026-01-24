import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):

    def test_isosceles_triangle(self):
        # Typical case: Isosceles triangle
        self.assertTrue(check_isosceles(3, 3, 4))

    def test_equilateral_triangle(self):
        # Typical case: Equilateral triangle
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_scalene_triangle(self):
        # Typical case: Scalene triangle
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_isosceles_with_zero(self):
        # Edge case: Isosceles triangle with zero side
        self.assertFalse(check_isosceles(0, 3, 3))

    def test_isosceles_with_negative(self):
        # Edge case: Isosceles triangle with negative side
        self.assertFalse(check_isosceles(-3, 3, 3))

    def test_isosceles_with_non_integer(self):
        # Edge case: Isosceles triangle with non-integer sides
        self.assertFalse(check_isosceles(3.1, 3.1, 4.1))
