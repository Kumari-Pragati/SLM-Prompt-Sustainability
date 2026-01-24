import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))
        self.assertFalse(is_not_prime(11))

    def test_composite_numbers(self):
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(10))
        self.assertTrue(is_not_prime(15))

    def test_edge_cases(self):
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(1))
        self.assertTrue(is_not_prime(2**64))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_not_prime, 'not_a_number')
        self.assertRaises(TypeError, is_not_prime, [1, 2, 3])
