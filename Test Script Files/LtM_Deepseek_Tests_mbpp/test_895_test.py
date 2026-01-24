import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([1]), 1)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([1, 2]), 2)
        self.assertEqual(max_sum_subseq([-1, -2]), -1)

    def test_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4]), 10)
        self.assertEqual(max_sum_subseq([5, 1, 1, 5]), 11)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4]), -1)
        self.assertEqual(max_sum_subseq([-5, -1, -1, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4]), 4)
        self.assertEqual(max_sum_subseq([-5, 1, -1, 5]), 6)

    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), None)

    def test_max_value(self):
        self.assertEqual(max_sum_subseq([1000000]), 1000000)

    def test_min_value(self):
        self.assertEqual(max_sum_subseq([-1000000]), -1000000)
