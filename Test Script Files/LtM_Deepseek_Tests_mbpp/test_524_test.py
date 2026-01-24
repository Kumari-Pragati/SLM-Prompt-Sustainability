import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 101, 100, 2, 3, 100], 6), 304)

    def test_edge_condition_empty_input(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(max_sum_increasing_subsequence([5], 1), 5)

    def test_edge_condition_all_same_elements(self):
        self.assertEqual(max_sum_increasing_subsequence([2, 2, 2, 2, 2], 5), 10)

    def test_complex_input(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subsequence("1,2,3,4,5", 5)
