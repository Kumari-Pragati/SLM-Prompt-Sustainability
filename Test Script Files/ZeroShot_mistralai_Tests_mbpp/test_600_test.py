import unittest
from six hundred import is_Even

class TestIsEven(unittest.TestCase):

    def test_zero(self):
        self.assertTrue(is_Even(0))

    def test_positive_even(self):
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(4))
        self.assertTrue(is_Even(6))

    def test_positive_odd(self):
        self.assertFalse(is_Even(1))
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(5))

    def test_negative_even(self):
        self.assertTrue(is_Even(-2))
        self.assertTrue(is_Even(-4))
        self.assertTrue(is_Even(-6))

    def test_negative_odd(self):
        self.assertFalse(is_Even(-1))
        self.assertFalse(is_Even(-3))
        self.assertFalse(is_Even(-5))
