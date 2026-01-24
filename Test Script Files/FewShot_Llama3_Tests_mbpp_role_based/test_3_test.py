import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertFalse(is_not_prime(2))

    def test_composite_number(self):
        self.assertTrue(is_not_prime(4))

    def test_prime_number_edge(self):
        self.assertFalse(is_not_prime(23))

    def test_composite_number_edge(self):
        self.assertTrue(is_not_prime(36))

    def test_zero(self):
        with self.assertRaises(ValueError):
            is_not_prime(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            is_not_prime(-1)
