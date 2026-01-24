import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(max_sum_subseq([-1]), -1)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([-1, 2]), 2)

    def test_three_elements(self):
        self.assertEqual(max_sum_subseq([-2, 1, 3]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_subseq([1, -2, 3, -4, 5]), 6)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            max_sum_subseq([])

    def test_single_element_list(self):
        self.assertEqual(max_sum_subseq([5]), 5)

    def test_all_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 5)

    def test_all_equal_numbers(self):
        self.assertEqual(max_sum_subseq([1, 1, 1, 1, 1]), 1)
