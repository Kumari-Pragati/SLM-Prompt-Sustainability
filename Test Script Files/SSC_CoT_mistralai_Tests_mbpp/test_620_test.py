import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(largest_subset([2, 3, 6, 7, 4, 12, 10], len(largest_subset([2, 3, 6, 7, 4, 12, 10]))), 6)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], len(largest_subset([1, 2, 3, 4, 5]))), 4)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(largest_subset([1], 1), 1)

    def test_edge_case_two_elements(self):
        self.assertEqual(largest_subset([1, 2], 2), 2)

    def test_edge_case_two_same_elements(self):
        self.assertEqual(largest_subset([2, 2], 2), 2)

    def test_edge_case_duplicate_elements(self):
        self.assertEqual(largest_subset([1, 2, 2, 3, 4], len(largest_subset([1, 2, 2, 3, 4]))), 4)

    def test_edge_case_all_divisible(self):
        self.assertEqual(largest_subset([2, 4, 6, 8], len(largest_subset([2, 4, 6, 8]))), 4)

    def test_edge_case_all_not_divisible(self):
        self.assertEqual(largest_subset([1, 3, 5, 7, 9], len(largest_subset([1, 3, 5, 7, 9]))), 1)

    def test_edge_case_all_zero(self):
        self.assertEqual(largest_subset([0, 0, 0], len(largest_subset([0, 0, 0]))), 0)

    def test_invalid_input_negative_list(self):
        with self.assertRaises(ValueError):
            largest_subset([-1, 2, 3], len(largest_subset([-1, 2, 3])))

    def test_invalid_input_negative_number(self):
        with self.assertRaises(ValueError):
            largest_subset([2, 3], -1)
