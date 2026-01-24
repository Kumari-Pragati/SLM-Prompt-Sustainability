import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_typical_odd(self):
        self.assertTrue(is_odd(3))

    def test_typical_even(self):
        self.assertFalse(is_odd(4))

    def test_edge_case_zero(self):
        self.assertFalse(is_odd(0))

    def test_edge_case_negative(self):
        self.assertTrue(is_odd(-3))

    def test_edge_case_positive(self):
        self.assertTrue(is_odd(1))

    def test_edge_case_large_positive(self):
        self.assertTrue(is_odd(1001))

    def test_edge_case_large_negative(self):
        self.assertTrue(is_odd(-1001))

    def test_edge_case_large_zero(self):
        self.assertFalse(is_odd(0))
