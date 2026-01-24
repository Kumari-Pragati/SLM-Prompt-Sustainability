import unittest
from mbpp_600_code import is_Even

class TestIsEven(unittest.TestCase):
    def test_typical_even(self):
        self.assertTrue(is_Even(4))

    def test_typical_odd(self):
        self.assertFalse(is_Even(3))

    def test_edge_case_zero(self):
        self.assertTrue(is_Even(0))

    def test_edge_case_negative(self):
        self.assertTrue(is_Even(-4))

    def test_edge_case_positive(self):
        self.assertTrue(is_Even(4))

    def test_edge_case_one(self):
        self.assertFalse(is_Even(1))

    def test_edge_case_minus_one(self):
        self.assertFalse(is_Even(-1))

    def test_edge_case_large_positive(self):
        self.assertTrue(is_Even(1000))

    def test_edge_case_large_negative(self):
        self.assertTrue(is_Even(-1000))

    def test_edge_case_large_zero(self):
        self.assertTrue(is_Even(0))

    def test_edge_case_large_negative_zero(self):
        self.assertTrue(is_Even(-0))
