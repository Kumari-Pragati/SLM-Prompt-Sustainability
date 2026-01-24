import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_simple_even(self):
        self.assertTrue(is_Even(4))

    def test_simple_odd(self):
        self.assertFalse(is_Even(3))

    def test_edge_zero(self):
        self.assertTrue(is_Even(0))

    def test_edge_negative(self):
        self.assertTrue(is_Even(-4))

    def test_edge_large(self):
        self.assertTrue(is_Even(1000))

    def test_edge_negative_large(self):
        self.assertTrue(is_Even(-1000))

    def test_edge_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            is_Even(0)

    def test_edge_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Even("hello")
