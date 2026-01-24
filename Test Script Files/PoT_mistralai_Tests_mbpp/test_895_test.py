import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(max_sum_subseq([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 15)
        self.assertEqual(max_sum_subseq([0, -1, 0, -2, 0, -1, 0, -2, 0]), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(max_sum_subseq([]), 0)
        self.assertEqual(max_sum_subseq([0]), 0)
        self.assertEqual(max_sum_subseq([-1]), -1)
        self.assertEqual(max_sum_subseq([1, -1]), 0)
        self.assertEqual(max_sum_subseq([-1, -1]), -1)
