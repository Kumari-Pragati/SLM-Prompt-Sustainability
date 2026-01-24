import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_Even(4))
        self.assertTrue(is_Even(10))
        self.assertTrue(is_Even(20))

    def test_odd_numbers(self):
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(9))
        self.assertFalse(is_Even(21))

    def test_edge_cases(self):
        self.assertTrue(is_Even(0))
        self.assertFalse(is_Even(-1))
        self.assertFalse(is_Even(-2))

    def test_negative_numbers(self):
        self.assertFalse(is_Even(-4))
        self.assertFalse(is_Even(-10))
        self.assertFalse(is_Even(-20))

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            is_Even("hello")
        with self.assertRaises(TypeError):
            is_Even(3.14)
