import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))

    def test_composite_numbers(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertTrue(is_not_prime(9))

    def test_edge_cases(self):
        self.assertFalse(is_not_prime(10))
        self.assertFalse(is_not_prime(11))
        self.assertFalse(is_not_prime(29))
        self.assertFalse(is_not_prime(31))

    def test_large_numbers(self):
        self.assertTrue(is_not_prime(100))
        self.assertTrue(is_not_prime(1000))
        self.assertTrue(is_not_prime(10000))

    def test_negative_numbers(self):
        self.assertRaises(ValueError, is_not_prime, -1)
        self.assertRaises(ValueError, is_not_prime, 0)
