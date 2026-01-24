import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 101, 2, 3, 100, 4, 5]
        n = len(a)
        index = 3
        k = 5
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 205)

    def test_edge_case_single_element(self):
        a = [1]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)

    def test_boundary_case_empty_list(self):
        a = []
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 0)

    def test_corner_case_decreasing_sequence(self):
        a = [5, 4, 3, 2, 1]
        n = len(a)
        index = 0
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 10)

    def test_corner_case_duplicate_elements(self):
        a = [1, 2, 3, 2, 1]
        n = len(a)
        index = 0
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 7)

    def test_invalid_input(self):
        a = [1, 2, 3]
        n = -1
        index = 0
        k = 0
        with self.assertRaises(Exception):
            max_sum_increasing_subseq(a, n, index, k)
