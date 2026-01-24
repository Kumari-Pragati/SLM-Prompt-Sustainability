import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_Even(4))
        self.assertTrue(is_Even(10))
        self.assertTrue(is_Even(20))

    def test_odd_numbers(self):
        self.assertFalse(is_Even(1))
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(7))

    def test_edge_cases(self):
        self.assertTrue(is_Even(0))
        self.assertFalse(is_Even(-1))
        self.assertFalse(is_Even(-3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Even('a')
        with self.assertRaises(TypeError):
            is_Even(None)
