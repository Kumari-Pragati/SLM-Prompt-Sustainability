import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 101, 2, 3, 100, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 106)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_single_element_array(self):
        arr = [5]
        n = 1
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 5)

    def test_all_increasing_sequence(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 15)

    def test_all_decreasing_sequence(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 5)

    def test_same_elements_array(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 1)

    def test_negative_elements_array(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)
