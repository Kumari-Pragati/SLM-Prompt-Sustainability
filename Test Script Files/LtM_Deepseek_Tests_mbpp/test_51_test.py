import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_simple_equilateral(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_simple_non_equilateral(self):
        self.assertFalse(check_equilateral(3, 4, 5))

    def test_negative_numbers(self):
        self.assertTrue(check_equilateral(-3, -3, -3))
        self.assertFalse(check_equilateral(-3, -4, -5))

    def test_zero(self):
        self.assertTrue(check_equilateral(0, 0, 0))
        self.assertFalse(check_equilateral(0, 1, 2))

    def test_mixed_positive_and_negative(self):
        self.assertFalse(check_equilateral(-3, 3, 3))
        self.assertFalse(check_equilateral(3, -3, -3))
        self.assertFalse(check_equilateral(-3, -3, 3))

    def test_large_numbers(self):
        self.assertTrue(check_equilateral(1000000, 1000000, 1000000))
        self.assertFalse(check_equilateral(1000000, 999999, 1000001))
