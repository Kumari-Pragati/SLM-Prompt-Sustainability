import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([1]), 1)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([1, 2]), 2)

    def test_three_elements(self):
        self.assertEqual(max_sum_subseq([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3]), -1)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(max_sum_subseq([1, -2, 3, -4, 5]), 6)

    def test_all_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 10)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            max_sum_subseq([])

    def test_single_element_list(self):
        with self.assertRaises(IndexError):
            max_sum_subseq([1])
