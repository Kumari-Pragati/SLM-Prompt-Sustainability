import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6], 6), 5)

    def test_edge_case_missing_first(self):
        self.assertEqual(find_missing([2, 3, 4, 5, 6], 6), 1)

    def test_edge_case_missing_last(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 6), 6)

    def test_boundary_case_single_element(self):
        self.assertEqual(find_missing([1], 1), -1)

    def test_boundary_case_empty_list(self):
        self.assertEqual(find_missing([], 0), -1)

    def test_invalid_input_negative_N(self):
        with self.assertRaises(ValueError):
            find_missing([1, 2, 3, 4, 5], -1)

    def test_invalid_input_N_greater_than_length(self):
        with self.assertRaises(ValueError):
            find_missing([1, 2, 3, 4, 5], 6)

    def test_invalid_input_non_integer_N(self):
        with self.assertRaises(TypeError):
            find_missing([1, 2, 3, 4, 5], '6')
