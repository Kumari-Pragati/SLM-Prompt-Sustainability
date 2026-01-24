import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))

    def test_edge_cases(self):
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(1))
        self.assertTrue(is_not_prime(100))
        self.assertTrue(is_not_prime(1000))

    def test_boundary_cases(self):
        self.assertFalse(is_not_prime(2))
        self.assertTrue(is_not_prime(3))
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(2**31 - 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_not_prime("15")
        with self.assertRaises(ValueError):
            is_not_prime(-5)
