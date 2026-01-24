import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_positive_odd_number(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))

    def test_zero(self):
        self.assertFalse(is_odd(0))

    def test_negative_odd_number(self):
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(-3))
        self.assertTrue(is_odd(-5))

    def test_positive_even_number(self):
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(6))

    def test_negative_even_number(self):
        self.assertFalse(is_odd(-2))
        self.assertFalse(is_odd(-4))
        self.assertFalse(is_odd(-6))

    def test_non_integer_input(self):
        self.assertRaises(TypeError, is_odd, 3.14)
        self.assertRaises(TypeError, is_odd, "string")
