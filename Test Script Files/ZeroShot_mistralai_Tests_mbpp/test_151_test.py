import unittest
from mbpp_151_code import is_coprime, gcd

class TestIsCoprime(unittest.TestCase):

    def test_is_coprime_positive_numbers(self):
        self.assertTrue(is_coprime(3, 5))
        self.assertTrue(is_coprime(7, 11))
        self.assertTrue(is_coprime(29, 41))

    def test_is_not_coprime_positive_numbers(self):
        self.assertFalse(is_coprime(3, 6))
        self.assertFalse(is_coprime(5, 10))
        self.assertFalse(is_coprime(15, 20))

    def test_is_coprime_zero_and_negative_numbers(self):
        self.assertFalse(is_coprime(0, 5))
        self.assertFalse(is_coprime(-3, 5))
        self.assertFalse(is_coprime(3, -5))

    def test_is_coprime_same_number(self):
        self.assertTrue(is_coprime(2, 2))
        self.assertTrue(is_coprime(4, 4))
        self.assertTrue(is_coprime(8, 8))
