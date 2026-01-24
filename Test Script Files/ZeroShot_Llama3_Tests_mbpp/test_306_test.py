import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_max_sum_increasing_subseq(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 4), 9)
        self.assertEqual(max_sum_increasing_subseq([5, 4, 3, 2, 1], 5, 0, 4), 5)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 1, 2), 5)
        self.assertEqual(max_sum_increasing_subseq([5, 4, 3, 2, 1], 5, 1, 2), 3)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([5, 4, 3, 2, 1], 5, 0, 0), 5)

    def test_max_sum_increasing_subseq_edge_cases(self):
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([5], 1, 0, 0), 5)
        self.assertEqual(max_sum_increasing_subseq([1, 2], 2, 0, 1), 3)
        self.assertEqual(max_sum_increasing_subseq([2, 1], 2, 0, 1), 2)
