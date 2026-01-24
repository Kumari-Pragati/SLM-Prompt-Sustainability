import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_positive_odd_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(7))
        self.assertTrue(is_odd(99))

    def test_zero(self):
        self.assertFalse(is_odd(0))

    def test_negative_numbers(self):
        self.assertFalse(is_odd(-1))
        self.assertFalse(is_odd(-3))
        self.assertFalse(is_odd(-5))

    def test_edge_cases(self):
        self.assertTrue(is_odd(2**16 - 1))  # maximum positive int
        self.assertFalse(is_odd(-2**16))  # minimum negative int
        self.assertFalse(is_odd(0b1))  # binary 1
        self.assertTrue(is_odd(0b11))  # binary 3
        self.assertFalse(is_odd(0o1))  # octal 1
        self.assertTrue(is_odd(0o3))  # octal 3
        self.assertFalse(is_odd(0x1))  # hexadecimal 1
        self.assertTrue(is_odd(0x3))  # hexadecimal 3
