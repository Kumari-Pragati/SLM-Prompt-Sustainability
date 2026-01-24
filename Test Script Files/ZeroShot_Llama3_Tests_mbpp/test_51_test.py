import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_equilateral(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_not_equilateral(self):
        self.assertFalse(check_equilateral(1, 2, 3))

    def test_equilateral_with_negative_numbers(self):
        self.assertTrue(check_equilateral(-3, -3, -3))

    def test_not_equilateral_with_negative_numbers(self):
        self.assertFalse(check_equilateral(-1, -2, -3))

    def test_equilateral_with_zero(self):
        self.assertFalse(check_equilateral(0, 0, 0))

    def test_equilateral_with_zero_and_positive(self):
        self.assertFalse(check_equilateral(0, 3, 3))

    def test_equilateral_with_zero_and_negative(self):
        self.assertFalse(check_equilateral(0, -3, -3))
