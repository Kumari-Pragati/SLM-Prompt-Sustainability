import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_coprime_numbers(self):
        self.assertTrue(is_coprime(2, 3))

    def test_coprime_numbers_with_negative(self):
        self.assertTrue(is_coprime(-2, 3))

    def test_coprime_numbers_with_zero(self):
        self.assertFalse(is_coprime(0, 3))

    def test_coprime_numbers_with_one(self):
        self.assertFalse(is_coprime(1, 3))

    def test_non_coprime_numbers(self):
        self.assertFalse(is_coprime(2, 4))

    def test_non_coprime_numbers_with_negative(self):
        self.assertFalse(is_coprime(-2, 4))

    def test_non_coprime_numbers_with_zero(self):
        self.assertFalse(is_coprime(0, 4))

    def test_non_coprime_numbers_with_one(self):
        self.assertFalse(is_coprime(1, 4))
