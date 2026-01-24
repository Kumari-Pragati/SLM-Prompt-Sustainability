import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):
    def test_typical_case(self):
        a = [1, 101, 2, 3, 100, 4, 5]
        n = len(a)
        index = 3
        k = 5
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 106)

    def test_edge_case_small_array(self):
        a = [1, 2, 3]
        n = len(a)
        index = 0
        k = 2
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 6)

    def test_boundary_case_large_array(self):
        a = list(range(1, 1001))
        n = len(a)
        index = 0
        k = 1000
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), sum(a))

    def test_invalid_input_negative_numbers(self):
        a = [-1, -2, -3]
        n = len(a)
        index = 0
        k = 2
        self.assertRaises(Exception, max_sum_increasing_subseq, a, n, index, k)

    def test_invalid_input_non_increasing_sequence(self):
        a = [3, 2, 1]
        n = len(a)
        index = 0
        k = 2
        self.assertRaises(Exception, max_sum_increasing_subseq, a, n, index, k)
