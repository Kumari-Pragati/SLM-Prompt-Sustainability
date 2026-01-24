import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 101, 2, 3, 100, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 103)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 5)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_sum_increasing_subsequence(arr, n), 0)

    def test_invalid_input_non_integer_elements(self):
        arr = [1, 2, '3', 4, 5]
        n = len(arr)
        with self.assertRaises(TypeError):
            max_sum_increasing_subsequence(arr, n)
