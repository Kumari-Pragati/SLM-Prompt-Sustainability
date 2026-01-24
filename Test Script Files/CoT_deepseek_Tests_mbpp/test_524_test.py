import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 101, 2, 3, 100, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 106)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 5)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_all_same_elements(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 1)

    def test_decreasing_sequence(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 15000)
