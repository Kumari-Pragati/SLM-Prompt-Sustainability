import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_non_equilateral_triangle(self):
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_zero_triangle(self):
        self.assertFalse(check_equilateral(0, 0, 0))

    def test_negative_triangle(self):
        self.assertFalse(check_equilateral(-1, -1, -1))

    def test_one_equal_two_different(self):
        self.assertFalse(check_equilateral(1, 2, 1))
