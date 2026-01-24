import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 2, 3), 7)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)

    def test_edge_case_decreasing_sequence(self):
        self.assertEqual(max_sum_increasing_subseq([4, 3, 2, 1], 4, 3, 3), 6)

    def test_edge_case_increasing_sequence(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 0, 3), 10)

    def test_edge_case_index_out_of_bounds(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 5, 0), 0)

    def test_edge_case_k_out_of_bounds(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4], 4, 0, 5), 0)
