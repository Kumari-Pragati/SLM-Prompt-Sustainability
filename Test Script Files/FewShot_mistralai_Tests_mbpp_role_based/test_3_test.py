import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(10))

    def test_composite_number(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))

    def test_zero(self):
        self.assertFalse(is_not_prime(0))

    def test_negative_number(self):
        self.assertFalse(is_not_prime(-1))

    def test_large_number(self):
        self.assertTrue(is_not_prime(1000000007))
