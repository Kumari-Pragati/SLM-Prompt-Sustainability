import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_subset([10, 5, 20, 15], 4), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(largest_subset([1], 1), 1)

    def test_boundary_case_empty_list(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(largest_subset([10, 10, 10, 10], 4), 4)

    def test_corner_case_large_input(self):
        self.assertEqual(largest_subset(list(range(1, 1001)), 1000), 500)

    def test_corner_case_small_input(self):
        self.assertEqual(largest_subset([1, 2, 4, 8, 16], 5), 5)

    def test_corner_case_large_and_small_elements(self):
        self.assertEqual(largest_subset([1000, 2, 500, 10], 4), 3)

    def test_corner_case_negative_elements(self):
        self.assertEqual(largest_subset([-10, -5, 10, 5], 4), 2)

    def test_corner_case_zero_element(self):
        self.assertEqual(largest_subset([0, 1, 2, 3], 4), 4)
