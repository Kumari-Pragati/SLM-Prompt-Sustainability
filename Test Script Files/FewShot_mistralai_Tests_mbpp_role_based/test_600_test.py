import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_Even(0))
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(4))
        self.assertTrue(is_Even(6))

    def test_odd_number(self):
        self.assertFalse(is_Even(1))
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(5))
        self.assertFalse(is_Even(7))

    def test_negative_number(self):
        self.assertTrue(is_Even(-0))
        self.assertTrue(is_Even(-2))
        self.assertTrue(is_Even(-4))
        self.assertTrue(is_Even(-6))

    def test_zero_or_one(self):
        self.assertFalse(is_Even(0))
        self.assertFalse(is_Even(1))
