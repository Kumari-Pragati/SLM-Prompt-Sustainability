import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_subset([10, 5, 20, 15], 4), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(largest_subset([1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_edge_case_all_elements_same(self):
        self.assertEqual(largest_subset([10, 10, 10, 10], 4), 4)

    def test_edge_case_all_elements_divisible(self):
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], 5), 5)

    def test_explicitly_handled_error_case_negative_numbers(self):
        with self.assertRaises(Exception):
            largest_subset([-1, -2, -3], 3)

    def test_explicitly_handled_error_case_zero(self):
        with self.assertRaises(Exception):
            largest_subset([0, 0, 0], 3)
