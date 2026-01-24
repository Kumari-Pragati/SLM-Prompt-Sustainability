import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 5, 3, 8, 9, 2]
        n = len(a)
        index = 2
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 13)

    def test_empty_list(self):
        a = []
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 0)

    def test_single_element_list(self):
        a = [1]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_decreasing_sequence(self):
        a = [8, 7, 6, 5, 4]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 19)

    def test_negative_numbers(self):
        a = [-1, -2, -3, -4, -5]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), -6)

    def test_invalid_index(self):
        a = [1, 5, 3, 8, 9, 2]
        n = len(a)
        index = n + 1
        k = 4
        self.assertRaises(IndexError, max_sum_increasing_subseq, a, n, index, k)

    def test_invalid_k(self):
        a = [1, 5, 3, 8, 9, 2]
        n = len(a)
        index = 2
        k = -1
        self.assertRaises(ValueError, max_sum_increasing_subseq, a, n, index, k)
