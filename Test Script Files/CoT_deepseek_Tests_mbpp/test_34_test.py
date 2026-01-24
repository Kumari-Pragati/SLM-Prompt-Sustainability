import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6], 6), 5)

    def test_edge_case_missing_first(self):
        self.assertEqual(find_missing([2, 3, 4, 5, 6], 6), 1)

    def test_edge_case_missing_last(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 6), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(find_missing([1], 1), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(find_missing([], 0), -1)

    def test_invalid_input_negative_N(self):
        with self.assertRaises(Exception):
            find_missing([1, 2, 3, 4, 5], -1)

    def test_invalid_input_N_greater_than_length_of_array(self):
        with self.assertRaises(Exception):
            find_missing([1, 2, 3, 4, 5], 6)

    def test_invalid_input_array_with_duplicates(self):
        with self.assertRaises(Exception):
            find_missing([1, 2, 2, 4, 5], 5)
