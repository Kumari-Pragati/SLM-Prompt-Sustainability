import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_is_odd_positive(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))

    def test_is_odd_negative(self):
        self.assertFalse(is_odd(-1))
        self.assertFalse(is_odd(-3))
        self.assertFalse(is_odd(-5))
        self.assertTrue(is_odd(-2))
        self.assertTrue(is_odd(-4))

    def test_is_odd_zero(self):
        self.assertFalse(is_odd(0))
