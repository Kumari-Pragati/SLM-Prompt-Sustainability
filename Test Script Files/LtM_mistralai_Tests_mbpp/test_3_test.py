import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_simple_not_prime(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(9))

    def test_simple_prime(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))

    def test_edge_cases(self):
        self.assertTrue(is_not_prime(0))
        self.assertTrue(is_not_prime(1))
        self.assertTrue(is_not_prime(2**64))
