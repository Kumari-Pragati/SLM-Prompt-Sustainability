import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 101, 100, 2, 3, 100, 4, 5], 8), 304)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum_increasing_subsequence([5], 1), 5)

    def test_edge_case_empty_array(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_corner_case_all_elements_same(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 1, 1, 1, 1], 5), 5)

    def test_corner_case_all_elements_increasing(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 15)

    def test_corner_case_all_elements_decreasing(self):
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 15)

    def test_corner_case_all_elements_increasing_with_duplicates(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 2, 3, 4, 4, 5], 7), 15)
