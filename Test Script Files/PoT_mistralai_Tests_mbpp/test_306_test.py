import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 5, 3, 9, 10], 5, 2, 4), 19)
        self.assertEqual(max_sum_increasing_subseq([2, 3, 4, 5], 4, 3, 3), 12)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6], 6, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5, 6], 6, 5, 5), 6)

    def test_edge_cases(self):
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([1, 2], 2, 1, 1), 3)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 2, 2), 5)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 3, 3), 7)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 4), 9)

    def test_corner_cases(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 2, 3, 2, 1], 6, 4, 4), 7)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 2, 1, 2, 3], 6, 5, 5), 7)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 2, 2, 1, 2], 6, 4, 4), 6)
        self.assertEqual(max_sum_increasing_subseq([2, 1, 2, 2, 1, 2], 6, 5, 5), 6)
