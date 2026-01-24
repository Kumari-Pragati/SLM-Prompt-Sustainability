import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_sum_subseq([1]), 1)
        self.assertEqual(max_sum_subseq([2, 3]), 3)
        self.assertEqual(max_sum_subseq([-1, -2, -3]), -1)
        self.assertEqual(max_sum_subseq([1, 2, 3]), 3)
        self.assertEqual(max_sum_subseq([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(max_sum_subseq([]), 0)
        self.assertEqual(max_sum_subseq([-1000000]), -1000000)
        self.assertEqual(max_sum_subseq([1000000]), 1000000)

    def test_complex_cases(self):
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5, 6]), 6)
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5, 6, -7, 8]), 8)
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]), 10)
