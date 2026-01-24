import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_non_equilateral_triangle(self):
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_equilateral_triangle_with_negative_values(self):
        self.assertTrue(check_equilateral(-3, -3, -3))

    def test_non_equilateral_triangle_with_negative_values(self):
        self.assertFalse(check_equilateral(-3, -4, -5))

    def test_equilateral_triangle_with_zero(self):
        self.assertTrue(check_equilateral(0, 0, 0))

    def test_non_equilateral_triangle_with_zero(self):
        self.assertFalse(check_equilateral(0, 1, 2))
