import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_positive_odd_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(7))

    def test_positive_even_numbers(self):
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(6))
        self.assertFalse(is_odd(8))

    def test_negative_odd_numbers(self):
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(-3))
        self.assertTrue(is_odd(-5))
        self.assertTrue(is_odd(-7))

    def test_negative_even_numbers(self):
        self.assertFalse(is_odd(-2))
        self.assertFalse(is_odd(-4))
        self.assertFalse(is_odd(-6))
        self.assertFalse(is_odd(-8))

    def test_zero(self):
        self.assertFalse(is_odd(0))

    def test_large_numbers(self):
        self.assertTrue(is_odd(9999999999999999999))
        self.assertFalse(is_odd(10000000000000000000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_odd('a')
        with self.assertRaises(TypeError):
            is_odd(None)
