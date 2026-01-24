import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_increasing_subseq([], len([]), 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum_increasing_subseq([1], len([1]), 0, 0), 1)

    def test_simple_case(self):
        self.assertEqual(max_sum_increasing_subseq([1, 5, 3, 4, 2], len([1, 5, 3, 4, 2]), 0, 0), 7)

    def test_case_with_zero(self):
        self.assertEqual(max_sum_increasing_subseq([1, 5, 3, 0, 2], len([1, 5, 3, 0, 2]), 0, 0), 8)

    def test_case_with_negative_numbers(self):
        self.assertEqual(max_sum_increasing_subseq([-1, -5, 3, 4, -2], len([-1, -5, 3, 4, -2]), 0, 0), 5)

    def test_case_with_large_numbers(self):
        self.assertEqual(max_sum_increasing_subseq([1000000001, 1000000002, 1000000003, 1000000004, 1000000005], len([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]), 0, 0), 2500000015)

    def test_case_with_index(self):
        self.assertEqual(max_sum_increasing_subseq([1, 5, 3, 4, 2], len([1, 5, 3, 4, 2]), 2, 0), 5)

    def test_case_with_k(self):
        self.assertEqual(max_sum_increasing_subseq([1, 5, 3, 4, 2], len([1, 5, 3, 4, 2]), 0, 2), 7)
