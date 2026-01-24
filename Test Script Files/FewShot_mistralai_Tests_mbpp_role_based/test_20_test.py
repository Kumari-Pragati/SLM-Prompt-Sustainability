import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_positive_even_numbers(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))

    def test_positive_odd_numbers(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(3))
        self.assertTrue(is_woodall(5))
        self.assertTrue(is_woodall(7))

    def test_zero(self):
        self.assertFalse(is_woodall(0))

    def test_negative_numbers(self):
        self.assertFalse(is_woodall(-1))
        self.assertFalse(is_woodall(-2))
        self.assertFalse(is_woodall(-3))
