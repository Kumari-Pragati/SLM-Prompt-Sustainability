import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))

    def test_non_prime_number(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertTrue(is_not_prime(9))

    def test_negative_number(self):
        self.assertTrue(is_not_prime(-1))
        self.assertTrue(is_not_prime(-2))
        self.assertTrue(is_not_prime(-3))

    def test_zero_and_one(self):
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(1))

    def test_large_prime_number(self):
        self.assertFalse(is_not_prime(1000003))
