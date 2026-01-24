import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_positive_odd(self):
        self.assertTrue(is_odd(5))

    def test_positive_even(self):
        self.assertFalse(is_odd(4))

    def test_negative_odd(self):
        self.assertTrue(is_odd(-5))

    def test_negative_even(self):
        self.assertFalse(is_odd(-4))

    def test_zero(self):
        self.assertFalse(is_odd(0))
