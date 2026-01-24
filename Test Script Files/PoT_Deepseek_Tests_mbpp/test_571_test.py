import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 2), 6)

    def test_edge_case_with_single_element(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 10), 0)

    def test_boundary_case_with_two_elements(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 1), 3)

    def test_corner_case_with_sorted_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 6), 15)

    def test_corner_case_with_reverse_sorted_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([5, 4, 3, 2, 1], 5, 6), 15)

    def test_corner_case_with_duplicate_elements(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 2, 3, 4], 5, 2), 6)

    def test_invalid_input_case_with_negative_numbers(self):
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K([-1, -2, -3, -4], 4, 2)

    def test_invalid_input_case_with_negative_K(self):
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, -2)
