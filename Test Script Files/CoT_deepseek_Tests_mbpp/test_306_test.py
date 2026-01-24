import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 101, 2, 3, 100, 4, 5]
        n = len(a)
        index = 3
        k = 5
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 106)

    def test_single_element(self):
        a = [1]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_decreasing_sequence(self):
        a = [5, 4, 3, 2, 1]
        n = len(a)
        index = 0
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 0)

    def test_invalid_index(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 6
        k = 4
        with self.assertRaises(IndexError):
            max_sum_increasing_subseq(a, n, index, k)

    def test_invalid_k(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 3
        k = 6
        with self.assertRaises(IndexError):
            max_sum_increasing_subseq(a, n, index, k)
