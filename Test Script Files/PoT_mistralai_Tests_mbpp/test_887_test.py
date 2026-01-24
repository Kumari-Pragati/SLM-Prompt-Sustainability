import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(7))

    def test_edge_cases(self):
        self.assertTrue(is_odd(0))
        self.assertFalse(is_odd(-1))
        self.assertTrue(is_odd(2**31 - 1))
        self.assertTrue(is_odd(-2**31 + 1))

    def test_corner_cases(self):
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(10**100))
        self.assertFalse(is_odd(-10**100))
