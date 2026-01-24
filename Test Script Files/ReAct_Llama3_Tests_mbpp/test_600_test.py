import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_Even(4))

    def test_odd_numbers(self):
        self.assertFalse(is_Even(3))

    def test_zero(self):
        self.assertTrue(is_Even(0))

    def test_negative_numbers(self):
        self.assertTrue(is_Even(-4))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_Even('a')

    def test_edge_case(self):
        self.assertTrue(is_Even(2**31 - 1))
