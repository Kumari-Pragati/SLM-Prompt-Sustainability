import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 100, 2, 3, 102], 6, 2, 5), 304)

    def test_edge_conditions(self):
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([1, 2], 2, 0, 1), 3)
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3], 3, 0, 2), 6)

    def test_complex_cases(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 3), 15)
        self.assertEqual(max_sum_increasing_subseq([5, 4, 3, 2, 1], 5, 0, 4), 15)
        self.assertEqual(max_sum_increasing_subseq([1, 101, 100, 2, 3, 102], 6, 1, 3), 303)
