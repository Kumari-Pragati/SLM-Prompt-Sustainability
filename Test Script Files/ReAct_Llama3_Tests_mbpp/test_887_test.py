import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_even_numbers(self):
        self.assertFalse(is_odd(4))

    def test_odd_numbers(self):
        self.assertTrue(is_odd(5))

    def test_zero(self):
        self.assertFalse(is_odd(0))

    def test_negative_numbers(self):
        self.assertFalse(is_odd(-3))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_odd('a')

    def test_edge_case(self):
        self.assertTrue(is_odd(1))
