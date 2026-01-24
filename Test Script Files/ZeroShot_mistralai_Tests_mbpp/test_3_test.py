import unittest
from mbpp_3_code import is_not_prime
import math

class TestIsNotPrime(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(25))
        self.assertTrue(is_not_prime(49))

        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))

    def test_composite_numbers(self):
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertTrue(is_not_prime(10))
        self.assertTrue(is_not_prime(15))

    def test_large_numbers(self):
        self.assertTrue(is_not_prime(28))
        self.assertTrue(is_not_prime(44))
        self.assertTrue(is_not_prime(77))
        self.assertTrue(is_not_prime(100))
