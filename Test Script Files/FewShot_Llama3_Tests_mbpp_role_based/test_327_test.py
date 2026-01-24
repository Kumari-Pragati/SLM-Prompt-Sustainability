import unittest
from mbpp_327_code import check_isosceles

class TestCheckIsosceles(unittest.TestCase):
    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 4))

    def test_isosceles_triangle_reversed(self):
        self.assertTrue(check_isosceles(4, 3, 3))

    def test_not_isosceles_triangle(self):
        self.assertFalse(check_isosceles(1, 2, 3))

    def test_isosceles_triangle_with_zero(self):
        self.assertFalse(check_isosceles(0, 0, 0))

    def test_isosceles_triangle_with_negative(self):
        self.assertFalse(check_isosceles(-1, -2, -3))
