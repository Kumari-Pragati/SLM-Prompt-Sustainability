import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 101, 100, 2, 3, 100, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 203)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 5)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_corner_case_decreasing_sequence(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 5)

    def test_corner_case_duplicate_elements(self):
        arr = [1, 101, 100, 2, 3, 100, 4, 5, 101]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 304)

    def test_invalid_input_negative_elements(self):
        arr = [-1, -101, -100, -2, -3, -100, -4, -5]
        n = len(arr)
        with self.assertRaises(Exception):
            max_sum_increasing_subsequence(arr, n)
