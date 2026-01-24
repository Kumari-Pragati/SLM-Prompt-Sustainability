import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(is_not_prime(4))

    def test_simple_false(self):
        self.assertFalse(is_not_prime(2))

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            is_not_prime(0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            is_not_prime(-1)

    def test_edge_case_one(self):
        self.assertFalse(is_not_prime(1))

    def test_edge_case_two(self):
        self.assertFalse(is_not_prime(2))

    def test_edge_case_large_prime(self):
        self.assertFalse(is_not_prime(23))

    def test_edge_case_large_non_prime(self):
        self.assertTrue(is_not_prime(24))

    def test_edge_case_large_prime_edge(self):
        self.assertFalse(is_not_prime(97))

    def test_edge_case_large_non_prime_edge(self):
        self.assertTrue(is_not_prime(98))

    def test_edge_case_large_prime_edge2(self):
        self.assertFalse(is_not_prime(101))

    def test_edge_case_large_non_prime_edge2(self):
        self.assertTrue(is_not_prime(102))
