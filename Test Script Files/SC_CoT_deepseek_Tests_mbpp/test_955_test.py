import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_abundant(12))

    def test_edge_case_smallest_abundant_number(self):
        self.assertTrue(is_abundant(12))

    def test_edge_case_largest_abundant_number(self):
        self.assertFalse(is_abundant(496))

    def test_edge_case_smallest_non_abundant_number(self):
        self.assertFalse(is_abundant(1))

    def test_edge_case_largest_non_abundant_number(self):
        self.assertFalse(is_abundant(28123))

    def test_invalid_input_negative_number(self):
        with self.assertRaises(Exception):
            is_abundant(-1)

    def test_invalid_input_zero(self):
        with self.assertRaises(Exception):
            is_abundant(0)

    def test_invalid_input_large_number(self):
        with self.assertRaises(Exception):
            is_abundant(28124)
