import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), 0)

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3]), -1)

    def test_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 15)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_subseq([1, -2, 3, -4, 5]), 7)

    def test_large_input(self):
        self.assertEqual(max_sum_subseq([100000, 100000, 100000]), 300000)
