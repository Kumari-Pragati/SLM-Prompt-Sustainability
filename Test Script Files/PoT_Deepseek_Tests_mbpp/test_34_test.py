import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6], 6), 5)

    def test_edge_case_with_single_element(self):
        self.assertEqual(find_missing([1], 1), -1)

    def test_boundary_case_with_two_elements(self):
        self.assertEqual(find_missing([1, 2], 2), -1)

    def test_corner_case_with_missing_first_element(self):
        self.assertEqual(find_missing([2, 3, 4, 5], 5), 1)

    def test_corner_case_with_missing_last_element(self):
        self.assertEqual(find_missing([1, 2, 3, 4], 5), 5)

    def test_corner_case_with_missing_middle_element(self):
        self.assertEqual(find_missing([1, 2, 4, 5], 5), 3)

    def test_invalid_input_with_negative_numbers(self):
        with self.assertRaises(Exception):
            find_missing([-1, 0, 1, 2, 3], 6)

    def test_invalid_input_with_non_integer_elements(self):
        with self.assertRaises(Exception):
            find_missing([1, 2, 3, 4.5, 5], 6)

    def test_invalid_input_with_duplicate_elements(self):
        with self.assertRaises(Exception):
            find_missing([1, 2, 2, 4, 5], 6)
