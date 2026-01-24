import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_typical_cases(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertFalse(is_not_prime(7))
        self.assertTrue(is_not_prime(8))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(is_not_prime(1))
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(5))
        self.assertTrue(is_not_prime(6))
        self.assertFalse(is_not_prime(7))
        self.assertTrue(is_not_prime(8))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(10))

    def test_corner_cases(self):
        self.assertFalse(is_not_prime(11))
        self.assertFalse(is_not_prime(12))
        self.assertTrue(is_not_prime(13))
        self.assertFalse(is_not_prime(14))
        self.assertTrue(is_not_prime(15))
        self.assertFalse(is_not_prime(16))
        self.assertTrue(is_not_prime(17))
        self.assertFalse(is_not_prime(18))
        self.assertTrue(is_not_prime(19))
        self.assertFalse(is_not_prime(20))
