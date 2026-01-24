import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_is_not_prime(self):
        self.assertTrue(is_not_prime(1))
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(10))
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))
        self.assertFalse(is_not_prime(11))
        self.assertFalse(is_not_prime(13))
        self.assertFalse(is_not_prime(17))
        self.assertFalse(is_not_prime(19))

    def test_edge_cases(self):
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(1))
