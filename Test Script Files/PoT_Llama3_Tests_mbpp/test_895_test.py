import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 9)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum_subseq([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(max_sum_subseq([1]), 1)

    def test_edge_case_two_element_list(self):
        self.assertEqual(max_sum_subseq([1, 2]), 2)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5]), 4)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 9)

    def test_edge_case_repeated_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 2, 3, 3, 3, 4, 5, 5]), 9)
