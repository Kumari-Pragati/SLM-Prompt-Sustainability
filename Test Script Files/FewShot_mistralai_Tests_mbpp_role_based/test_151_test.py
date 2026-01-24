import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_coprime_numbers(self):
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(29, 41))

    def test_not_coprime_numbers(self):
        self.assertFalse(is_coprime(6, 9))
        self.assertFalse(is_coprime(10, 20))

    def test_zero(self):
        self.assertFalse(is_coprime(0, 5))
        self.assertFalse(is_coprime(5, 0))

    def test_negative_numbers(self):
        self.assertFalse(is_coprime(-5, 3))
        self.assertFalse(is_coprime(3, -5))

    def test_same_number(self):
        self.assertFalse(is_coprime(4, 4))
