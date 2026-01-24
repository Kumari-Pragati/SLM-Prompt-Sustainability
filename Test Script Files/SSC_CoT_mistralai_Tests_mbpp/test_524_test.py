import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 5, 2, 9, 4], 5), 9)
        self.assertEqual(max_sum_increasing_subsequence([0, -1, 2, 3, 4], 5), 6)
        self.assertEqual(max_sum_increasing_subsequence([-3, -2, -1, 0, 1], 5), 1)

    def test_edge_cases(self):
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)
        self.assertEqual(max_sum_increasing_subsequence([1, 2], 2), 2)
        self.assertEqual(max_sum_increasing_subsequence([-1, -2], 2), -1)
        self.assertEqual(max_sum_increasing_subsequence([0], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3], 0), 0)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3], -1), 0)
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, max_sum_increasing_subsequence, [1, 2, 3], 'n')
        self.assertRaises(TypeError, max_sum_increasing_subsequence, [1, 2, 3], 1.5)
