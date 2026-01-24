import unittest
from mbpp_327_code import check_isosceles

class TestIsosceles(unittest.TestCase):

    def test_isosceles_triangle(self):
        self.assertTrue(check_isosceles(3, 3, 3))

    def test_not_isosceles_triangle_1(self):
        self.assertFalse(check_isosceles(3, 4, 5))

    def test_not_isosceles_triangle_2(self):
        self.assertFalse(check_isosceles(4, 3, 5))

    def test_not_isosceles_triangle_3(self):
        self.assertFalse(check_isosceles(4, 5, 3))

    def test_zero_or_negative_sides(self):
        self.assertFalse(check_isosceles(0, 3, 4))
        self.assertFalse(check_isosceles(-3, 3, 4))
        self.assertFalse(check_isosceles(3, 0, 4))
        self.assertFalse(check_isosceles(3, 4, 0))
        self.assertFalse(check_isosceles(0, 0, 0))
