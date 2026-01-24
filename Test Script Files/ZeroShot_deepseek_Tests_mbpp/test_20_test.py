import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_even_numbers(self):
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))

    def test_odd_numbers(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(15))
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(5))
        self.assertFalse(is_woodall(7))

    def test_large_numbers(self):
        self.assertTrue(is_woodall(16383))
        self.assertFalse(is_woodall(16384))
        self.assertFalse(is_woodall(16385))
