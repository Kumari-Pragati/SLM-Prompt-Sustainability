import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_coprime(3, 4))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    def test_negative_numbers(self):
        self.assertTrue(is_coprime(-3, -4))
        self.assertTrue(is_coprime(-5, -7))
        self.assertTrue(is_coprime(-11, -13))

    def test_mixed_numbers(self):
        self.assertTrue(is_coprime(-3, 4))
        self.assertTrue(is_coprime(5, -7))
        self.assertTrue(is_coprime(-11, 13))

    def test_zero(self):
        self.assertFalse(is_coprime(0, 4))
        self.assertFalse(is_coprime(5, 0))
        self.assertFalse(is_coprime(0, 0))

    def test_same_number(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertTrue(is_coprime(2, 2))
        self.assertTrue(is_coprime(3, 3))

    def test_large_numbers(self):
        self.assertTrue(is_coprime(1000000007, 1000000009))
        self.assertFalse(is_coprime(1000000008, 1000000010))
