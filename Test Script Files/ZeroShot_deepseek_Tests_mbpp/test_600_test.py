import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):

    def test_positive_even(self):
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(14))
        self.assertTrue(is_Even(100))

    def test_positive_odd(self):
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(15))
        self.assertFalse(is_Even(99))

    def test_negative_even(self):
        self.assertTrue(is_Even(-2))
        self.assertTrue(is_Even(-14))
        self.assertTrue(is_Even(-100))

    def test_negative_odd(self):
        self.assertFalse(is_Even(-3))
        self.assertFalse(is_Even(-15))
        self.assertFalse(is_Even(-99))

    def test_zero(self):
        self.assertTrue(is_Even(0))
