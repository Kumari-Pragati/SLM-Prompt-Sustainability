import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_abundant_number(self):
        self.assertTrue(is_abundant(12))

    def test_deficient_number(self):
        self.assertFalse(is_abundant(15))

    def test_perfect_number(self):
        self.assertTrue(is_abundant(6))

    def test_prime_number(self):
        self.assertFalse(is_abundant(7))

    def test_one(self):
        self.assertFalse(is_abundant(1))

    def test_zero(self):
        self.assertFalse(is_abundant(0))
