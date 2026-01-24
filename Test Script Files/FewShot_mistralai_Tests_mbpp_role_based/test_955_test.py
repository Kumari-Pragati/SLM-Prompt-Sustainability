import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_abundant_number(self):
        self.assertTrue(is_abundant(12))

    def test_non_abundant_number(self):
        self.assertFalse(is_abundant(11))

    def test_perfect_number(self):
        self.assertFalse(is_abundant(6))

    def test_small_number(self):
        self.assertFalse(is_abundant(1))

    def test_large_number(self):
        self.assertTrue(is_abundant(28))
