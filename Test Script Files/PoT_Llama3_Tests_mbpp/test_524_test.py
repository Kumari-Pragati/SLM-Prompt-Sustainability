import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case(self):
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 5)

    def test_edge_case2(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6], 6), 15)

    def test_edge_case3(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case4(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7], 7), 18)

    def test_edge_case5(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8], 8), 18)

    def test_edge_case6(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 18)

    def test_edge_case7(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 18)

    def test_edge_case8(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 18)

    def test_edge_case9(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 18)

    def test_edge_case10(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 18)

    def test_edge_case11(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 18)

    def test_edge_case12(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 18)

    def test_edge_case13(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 18)

    def test_edge_case14(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 18)

    def test_edge_case15(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 18)

    def test_edge_case16(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 18)

    def test_edge_case17(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7,