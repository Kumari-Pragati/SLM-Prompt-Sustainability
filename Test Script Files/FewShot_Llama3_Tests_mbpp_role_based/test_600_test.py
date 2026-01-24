import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_Even(4))

    def test_odd_number(self):
        self.assertFalse(is_Even(5))

    def test_zero(self):
        self.assertTrue(is_Even(0))

    def test_negative_number(self):
        self.assertTrue(is_Even(-4))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_Even('a')
