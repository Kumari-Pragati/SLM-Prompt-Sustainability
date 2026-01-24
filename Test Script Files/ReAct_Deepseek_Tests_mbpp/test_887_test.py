import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(0))

    def test_negative_numbers(self):
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(-3))
        self.assertFalse(is_odd(-2))
        self.assertFalse(is_odd(-4))

    def test_large_numbers(self):
        self.assertTrue(is_odd(9999999999999999999))
        self.assertFalse(is_odd(10000000000000000000))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_odd(1.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            is_odd('1')
