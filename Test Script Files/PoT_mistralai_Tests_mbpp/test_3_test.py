import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):

    def test_typical_cases(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(10))
        self.assertTrue(is_not_prime(15))
        self.assertTrue(is_not_prime(20))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(is_not_prime(1))
        self.assertTrue(is_not_prime(0))
        self.assertTrue(is_not_prime(-1))
        self.assertTrue(is_not_prime(2**64))
