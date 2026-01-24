import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([1]), 1)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([1, 2]), 2)
        self.assertEqual(max_sum_subseq([2, 1]), 2)

    def test_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3]), 6)
        self.assertEqual(max_sum_subseq([3, 2, 1]), 6)
        self.assertEqual(max_sum_subseq([1, 3, 2]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3]), -1)
        self.assertEqual(max_sum_subseq([-3, -2, -1]), -1)
        self.assertEqual(max_sum_subseq([-1, -3, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_subseq([-1, 2, -3]), 2)
        self.assertEqual(max_sum_subseq([-3, 2, -1]), 2)
        self.assertEqual(max_sum_subseq([-1, 2, 3]), 6)

    def test_empty_list(self):
        self.assertIsNone(max_sum_subseq([]))

    def test_large_input(self):
        self.assertEqual(max_sum_subseq(list(range(1, 1001))), 500500)
