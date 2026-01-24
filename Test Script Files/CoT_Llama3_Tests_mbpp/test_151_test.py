import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_coprime(self):
        self.assertTrue(is_coprime(1, 1))
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    def test_not_coprime(self):
        self.assertFalse(is_coprime(4, 2))
        self.assertFalse(is_coprime(6, 3))
        self.assertFalse(is_coprime(8, 4))
        self.assertFalse(is_coprime(9, 3))

    def test_zero(self):
        with self.assertRaises(ZeroDivisionError):
            is_coprime(0, 1)
        with self.assertRaises(ZeroDivisionError):
            is_coprime(1, 0)

    def test_negative(self):
        self.assertTrue(is_coprime(-1, 1))
        self.assertTrue(is_coprime(-2, 3))
        self.assertTrue(is_coprime(-5, 7))
        self.assertTrue(is_coprime(-11, 13))
