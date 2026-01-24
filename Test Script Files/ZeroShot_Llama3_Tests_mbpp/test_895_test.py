import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_max_sum_subseq(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 9)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_sum_subseq([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_sum_subseq([1, 1, 1, 1, 1]), 5)
        self.assertEqual(max_sum_subseq([-1, -1, -1, -1, -1]), -1)
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5, 6]), 10)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5, -6]), -1)
        self.assertEqual(max_sum_subseq([1, -2, 3, -4, 5, -6]), 5)
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5, 6]), 6)
        self.assertEqual(max_sum_subseq([1, 1, 1, 1, 1, 1]), 6)
        self.assertEqual(max_sum_subseq([-1, -1, -1, -1, -1, -1]), -1)
