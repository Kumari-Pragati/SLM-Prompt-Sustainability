import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 2, 4), 13)
        self.assertEqual(max_sum_increasing_subseq([10, 22, 9, 33, 21, 50, 41, 60, 80], 9, 4, 8), 161)

    def test_edge_cases(self):
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([1, 2], 2, 1, 1), 3)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 2), 5)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 3, 3), 7)

    def test_boundary_cases(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 4, 0), 4)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 3, 3), 7)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 0, 3), 1)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 4, 0), 4)

    def test_invalid_inputs(self):
        self.assertRaises(IndexError, max_sum_increasing_subseq, [1, 2, 3], -1, 0, 0)
        self.assertRaises(IndexError, max_sum_increasing_subseq, [1, 2, 3], 0, -1, 0)
        self.assertRaises(IndexError, max_sum_increasing_subseq, [1, 2, 3], 0, 0, -1)
        self.assertRaises(ValueError, max_sum_increasing_subseq, [1, 2, 3], 0, 0, 4)
        self.assertRaises(ValueError, max_sum_increasing_subseq, [1, 2, 3], 1, 0, 0)
