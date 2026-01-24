import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case2(self):
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 5)

    def test_edge_case3(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6], 6), 15)

    def test_edge_case4(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 0], 6), 10)

    def test_edge_case5(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, -1], 6), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subsequence("abc", 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subsequence([1, 2, 3], "abc")

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7], "abc")
