import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_coprime(self):
        self.assertTrue(is_coprime(1, 2))
        self.assertTrue(is_coprime(3, 4))
        self.assertTrue(is_coprime(5, 7))

    def test_not_coprime(self):
        self.assertFalse(is_coprime(4, 6))
        self.assertFalse(is_coprime(8, 12))
        self.assertFalse(is_coprime(15, 20))

    def test_edge_cases(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertFalse(is_coprime(2, 2))

    def test_zero_input(self):
        with self.assertRaises(ZeroDivisionError):
            is_coprime(0, 1)

    def test_negative_input(self):
        self.assertTrue(is_coprime(-1, 2))
        self.assertTrue(is_coprime(1, -2))

    def test_large_input(self):
        self.assertTrue(is_coprime(1000000, 2000000))
        self.assertTrue(is_coprime(2000000, 1000000))
