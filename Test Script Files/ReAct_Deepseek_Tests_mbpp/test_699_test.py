import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)

    def test_typical_case_with_duplicates(self):
        self.assertEqual(min_Swaps('aabb', 'abab'), 1)

    def test_edge_case_with_same_strings(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_edge_case_with_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_error_case_with_different_length_strings(self):
        with self.assertRaises(Exception):
            min_Swaps('abc', 'abcd')

    def test_error_case_with_non_string_inputs(self):
        with self.assertRaises(Exception):
            min_Swaps(123, 'abc')
        with self.assertRaises(Exception):
            min_Swaps('abc', 123)
