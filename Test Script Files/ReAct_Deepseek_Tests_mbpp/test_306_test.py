import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 101, 100, 2, 3, 102]
        n = len(a)
        index = 1
        k = 2
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 202)

    def test_edge_case_single_element(self):
        a = [1]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_edge_case_empty_list(self):
        a = []
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 0)

    def test_explicitly_handled_error_case_non_increasing_subseq(self):
        a = [100, 90, 80, 70]
        n = len(a)
        index = 0
        k = 1
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 0)

    def test_explicitly_handled_error_case_invalid_index(self):
        a = [1, 2, 3, 4]
        n = len(a)
        index = 5
        k = 1
        with self.assertRaises(IndexError):
            max_sum_increasing_subseq(a, n, index, k)

    def test_explicitly_handled_error_case_invalid_k(self):
        a = [1, 2, 3, 4]
        n = len(a)
        index = 0
        k = -1
        with self.assertRaises(ValueError):
            max_sum_increasing_subseq(a, n, index, k)
