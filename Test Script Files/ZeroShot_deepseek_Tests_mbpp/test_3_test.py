import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))
        self.assertFalse(is_not_prime(11))

    def test_non_prime_numbers(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(10))

    def test_negative_numbers(self):
        self.assertFalse(is_not_prime(-5))
        self.assertFalse(is_not_prime(-13))

    def test_zero_and_one(self):
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(1))
