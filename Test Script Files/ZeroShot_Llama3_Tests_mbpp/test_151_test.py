import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_coprime_positive_numbers(self):
        self.assertTrue(is_coprime(1, 2))
        self.assertTrue(is_coprime(3, 4))
        self.assertTrue(is_coprime(5, 6))
        self.assertTrue(is_coprime(7, 8))
        self.assertTrue(is_coprime(9, 10))

    def test_coprime_negative_numbers(self):
        self.assertTrue(is_coprime(-1, 2))
        self.assertTrue(is_coprime(3, -4))
        self.assertTrue(is_coprime(-5, 6))
        self.assertTrue(is_coprime(7, -8))
        self.assertTrue(is_coprime(-9, 10))

    def test_coprime_zero(self):
        with self.assertRaises(ZeroDivisionError):
            is_coprime(0, 2)
        with self.assertRaises(ZeroDivisionError):
            is_coprime(2, 0)

    def test_coprime_non_coprime_numbers(self):
        self.assertFalse(is_coprime(2, 4))
        self.assertFalse(is_coprime(3, 6))
        self.assertFalse(is_coprime(4, 8))
        self.assertFalse(is_coprime(5, 10))

    def test_coprime_edge_cases(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertTrue(is_coprime(-1, -1))
        self.assertTrue(is_coprime(0, 0))
