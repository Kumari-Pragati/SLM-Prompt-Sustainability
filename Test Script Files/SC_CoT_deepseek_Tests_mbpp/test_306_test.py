import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 100, 2, 3, 102], 6, 5, 3), 304)

    def test_edge_case(self):
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)

    def test_corner_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 3), 15)
        self.assertEqual(max_sum_increasing_subseq([5, 4, 3, 2, 1], 5, 4, 3), 15)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 6, 3)
        with self.assertRaises(Exception):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, -1, 3)
        with self.assertRaises(Exception):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, -1)
        with self.assertRaises(Exception):
            max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 0, 5)
