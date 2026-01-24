import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(1))
        self.assertFalse(is_not_prime(0))

    def test_edge_cases(self):
        self.assertFalse(is_not_prime(1))
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(-1))
        self.assertFalse(is_not_prime(-10))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            is_not_prime("not a number")
