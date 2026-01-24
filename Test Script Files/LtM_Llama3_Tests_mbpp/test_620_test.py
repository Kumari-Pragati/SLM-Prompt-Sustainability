import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(largest_subset([2, 4, 6, 8], 4), 4)

    def test_edge_case_empty_input(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_edge_case_single_element_input(self):
        self.assertEqual(largest_subset([5], 1), 1)

    def test_edge_case_all_divisible_input(self):
        self.assertEqual(largest_subset([2, 4, 6, 8, 10], 5), 5)

    def test_edge_case_all_non_divisible_input(self):
        self.assertEqual(largest_subset([1, 3, 5, 7, 9], 5), 1)

    def test_edge_case_mixed_divisible_input(self):
        self.assertEqual(largest_subset([2, 3, 4, 5, 6], 5), 4)

    def test_edge_case_max_subset_input(self):
        self.assertEqual(largest_subset([2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 10), 9)

    def test_edge_case_min_subset_input(self):
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)
