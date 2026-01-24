import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):

    def test_even_numbers(self):
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(4))
        self.assertTrue(is_Even(6))
        self.assertTrue(is_Even(8))

    def test_zero(self):
        self.assertTrue(is_Even(0))

    def test_negative_even_numbers(self):
        self.assertTrue(is_Even(-2))
        self.assertTrue(is_Even(-4))
        self.assertTrue(is_Even(-6))
        self.assertTrue(is_Even(-8))

    def test_odd_numbers(self):
        self.assertFalse(is_Even(1))
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(5))
        self.assertFalse(is_Even(7))

    def test_edge_cases(self):
        self.assertFalse(is_Even(-1))
        self.assertFalse(is_Even(0))
        self.assertFalse(is_Even(1))
