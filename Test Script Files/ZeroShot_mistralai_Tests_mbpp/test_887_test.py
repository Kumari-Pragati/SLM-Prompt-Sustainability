import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_is_odd_positive_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(7))
        self.assertTrue(is_odd(9))

    def test_is_odd_zero(self):
        self.assertFalse(is_odd(0))

    def test_is_odd_negative_numbers(self):
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(-3))
        self.assertTrue(is_odd(-5))
        self.assertTrue(is_odd(-7))

    def test_is_odd_edge_cases(self):
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(6))
        self.assertFalse(is_odd(8))
        self.assertFalse(is_odd(10))
